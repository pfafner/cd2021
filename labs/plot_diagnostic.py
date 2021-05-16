# Ciencia de Datos 2021
# Alan Reyes-Figueroa
# Archivo auxiliar para hacer los plots de diagnóstico para statsmodels.OLS

# Grafica los siguientes:
#    (1) Residuals vs. Fitted
#    (2) Residuals QQ-plot
#    (3) Scale-Location
#    (4) Residuals vs. Leverage


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

import seaborn as sns
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from statsmodels.graphics.gofplots import ProbPlot


def qq_plot(data):
    """
    Construct a qq-plot pairs for plotting based on data.
    """
    n = data.shape[0]
    qq = np.ones([n, 2])
    np.random.shuffle(data)
    x = np.linspace(0, 1, n+2)[1:-1]
    qq[:, 0] = np.sort(data)
    qq[:, 1] = norm.ppf(x)
    return qq



def graph(formula, x_range, label=None):
    """
    Helper function for plotting cook's distance lines
    """
    x = x_range
    y = formula(x)
    plt.plot(x, y, label=label, lw=1, ls='--', color='red')



def diagnostic_plots(X, y, model_fit=None):
    """
    Function to reproduce the 4 base plots of an OLS model (as in R).
    ---
    Inputs:
    X: pandas dataframe of the features to use in building the linear regression model,
    y: pandas series/dataframe of the target variable of the linear regression model,
    model_fit [optional]: a statsmodel.api.OLS model after regressing y on X. If not provided, will be
                          generated from X, y.
    """

    if not model_fit:
        model_fit = sm.OLS(y, sm.add_constant(X)).fit()

    # create dataframe from X, y for easier plot handling
    dataframe = pd.concat([X, y], axis=1)

    # model values
    model_fitted_y = model_fit.fittedvalues
    # model residuals
    model_residuals = model_fit.resid
    # normalized residuals
    model_norm_residuals = model_fit.get_influence().resid_studentized_internal
    # absolute squared normalized residuals
    model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
    # absolute residuals
    model_abs_resid = np.abs(model_residuals)
    # leverage, from statsmodels internals
    model_leverage = model_fit.get_influence().hat_matrix_diag
    # cook's distance, from statsmodels internals
    model_cooks = model_fit.get_influence().cooks_distance[0]

    # ---------- plot 1 ----------
    fig = plt.figure(figsize=(12,12))
    plot_lm_1 = fig.add_subplot(221)
    sns.residplot(model_fitted_y, dataframe.iloc[:,-1], data=dataframe, lowess=True,
                  scatter_kws={'alpha': 0.5}, line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
    plot_lm_1.set_title('Residuals vs Fitted')
    plot_lm_1.set_xlabel('Fitted values')
    plot_lm_1.set_ylabel('Residuals')
    # annotations
    abs_resid = model_abs_resid.sort_values(ascending=False)
    abs_resid_top_3 = abs_resid[:3]
    for i in abs_resid_top_3.index:
        plot_lm_1.annotate(i, xy=(model_fitted_y[i], model_residuals[i]))

    # ---------- plot 2 ----------
    plot_lm_2 = fig.add_subplot(222)
    QQ = ProbPlot(model_norm_residuals)
    #QQ.qqplot(line='45', alpha=0.5, color='#4C72B0', lw=1)
    #sm.qqplot(model_norm_residuals)
    #stats.probplot(model_norm_residuals, dist='norm')
    qq0 = model_norm_residuals - model_norm_residuals.mean()
    qq = qq_plot(qq0)
    mn, mx = min(qq.min(axis=0)), max(qq.max(axis=0))
    plt.scatter(qq[:,1], qq[:,0], alpha=0.5)
    sns.lineplot([mn,mx], [mn,mx], color='red', lw=1, alpha=0.8)
    plot_lm_2.set_title('Normal Q-Q')
    plot_lm_2.set_xlabel('Theoretical Quantiles')
    plot_lm_2.set_ylabel('Standardized Residuals')
    # annotations
    abs_norm_resid = np.flip(np.argsort(np.abs(model_norm_residuals)), 0)
    abs_norm_resid_top_3 = abs_norm_resid[:3]
    for r, i in enumerate(abs_norm_resid_top_3):
        plot_lm_2.annotate(i, xy=(np.flip(QQ.theoretical_quantiles, 0)[r], model_norm_residuals[i]))

    # ---------- plot 3 ----------
    plot_lm_3 = fig.add_subplot(223)
    plt.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5)
    sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt, scatter=False, ci=False, lowess=True,
                line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
    plot_lm_3.set_title('Scale-Location')
    plot_lm_3.set_xlabel('Fitted values')
    plot_lm_3.set_ylabel('$\sqrt{|Standardized Residuals|}$')
    # annotations
    abs_sq_norm_resid = np.flip(np.argsort(model_norm_residuals_abs_sqrt), 0)
    abs_sq_norm_resid_top_3 = abs_sq_norm_resid[:3]
    for i in abs_norm_resid_top_3:
        plot_lm_3.annotate(i, xy=(model_fitted_y[i], model_norm_residuals_abs_sqrt[i]))

    # ---------- plot 4 ----------
    plot_lm_4 = fig.add_subplot(224)
    plt.scatter(model_leverage, model_norm_residuals, alpha=0.5)
    sns.regplot(model_leverage, model_norm_residuals, scatter=False, ci=False, lowess=True,
                line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
    plot_lm_4.set_xlim(0, max(model_leverage)+0.01)
    plot_lm_4.set_ylim(-3, 5)
    plot_lm_4.set_title('Residuals vs Leverage')
    plot_lm_4.set_xlabel('Leverage')
    plot_lm_4.set_ylabel('Standardized Residuals')
    # annotations
    leverage_top_3 = np.flip(np.argsort(model_cooks), 0)[:3]
    for i in leverage_top_3:
        plot_lm_4.annotate(i, xy=(model_leverage[i], model_norm_residuals[i]))

    # ---------- adjustments ----------
    p = len(model_fit.params)  # number of model parameters
    graph(lambda x: np.sqrt((0.5 * p * (1 - x)) / x), np.linspace(0.001, max(model_leverage), 50), 'Cook\'s distance')
    # 0.5 line
    graph(lambda x: np.sqrt((1 * p * (1 - x)) / x), np.linspace(0.001, max(model_leverage), 50)) # 1 line
    #plot_lm_4.legend(loc='upper right')