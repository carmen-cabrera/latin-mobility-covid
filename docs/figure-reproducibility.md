# Figure reproducibility guide

This document maps manuscript figures and supplementary figures to the notebooks that generate the underlying analysis outputs or source plot panels.

The Meta-Facebook mobility and population datasets used in the study cannot be redistributed. For that reason, the public repository cannot regenerate figures end-to-end without approved access to the restricted data. In addition, several final manuscript figures and tables are assembled manually from script outputs generated locally. The purpose of this guide is to make that workflow more transparent, by identifying the scripts used to produce the source data, plot panels, model outputs or tables that were then combined into the final manuscript figures and tables.

## Main Manuscript Figures

| Manuscript figure | Description | Source scripts |
|---|---|---|
| Figure 1 | Overview of data inputs, calibration, analysis, validation and robustness checks. | Conceptual summary of the workflow implemented across `notebooks/preprocessing/` and `notebooks/analysis/`. Key preprocessing steps are in `notebooks/preprocessing/`, scripts 01 through 09; main analysis steps are in `notebooks/analysis/`, scripts 03, 05, 06, 08 and 09. |
| Figure 2 | Percentage change in mobility in May 2020 and March 2022 by population density and RDI category. | Generated from `notebooks/analysis/04-boxplots-before-after.ipynb`, which produces the before/after boxplot panels for density and RDI categories. |
| Figure 3 | Mixed-effects model estimates and recovery-time curves by population density and RDI category. | Generated from model outputs produced by `notebooks/analysis/05-trend-models.qmd` and recovery-time panels produced by `notebooks/analysis/06-recovery-times.ipynb`. |
| Figure 4 | Evolution of netflows involving capital urban regions and all functional urban areas by density category. | Generated from city/FUA netflow panels produced by `notebooks/analysis/07-mov-evolution-capital.ipynb`, with related city model and recovery-time outputs from `notebooks/analysis/08-city-trend-models.qmd` and `notebooks/analysis/09-city-recovery-times.ipynb`. |
| Figure 5 | Workflow diagram for the data imputation method. | Conceptual summary of the preprocessing workflow, especially the baseline-filling and imputation steps in `notebooks/preprocessing/`, scripts 03, 04, 05 and 08. |

## Supplementary Figures and Tables

| Supplementary item | Description | Source scripts |
|---|---|---|
| ST1 | Summary table of imputed records and imputed totals for Facebook Population and Facebook Movement data. | `notebooks/preprocessing/09-count-missing-values.ipynb` computes missingness/imputation summaries. |
| SF1 | Maps of missing and imputed Facebook Population baseline records. | `notebooks/preprocessing/05-impute-baseline-pop.ipynb` generates baseline population imputation outputs and map panels. |
| SF2-SF4 | Correlations between WorldPop population and Facebook Population counts during the baseline period. | `notebooks/preprocessing/05-impute-baseline-pop.ipynb` computes and plots baseline population validation/correlation diagnostics. |
| SF5-SF6 | Spatial interaction model validation and baseline movement checks. | `notebooks/preprocessing/08-impute-baseline-mov.ipynb` fits/checks the movement imputation model and produces diagnostic plots. |
| SF7 | Raw versus imputed mobility comparison at selected time points. | `notebooks/analysis/raw-sensitivity/04-raw-vs-imputed-summary.ipynb` reads raw and imputed outputs and creates comparison summaries. |
| ST2 | RDI component variables and source datasets. | Descriptive table based on NASA/SEDAC RDI documentation and manuscript methods; not generated from the restricted Facebook data. |
| SF8 | Maps of population density and RDI category classifications. | `notebooks/preprocessing/07-add-exo-var-to-baseline-pop.ipynb` creates the classified spatial units and map panels. |
| SF9 | Population shares by density/RDI category, comparing Facebook and WorldPop before/after imputation. | `notebooks/preprocessing/07-add-exo-var-to-baseline-pop.ipynb` generates category summaries after exogenous variables are added. |
| SF10 | Joint distribution of density and RDI categories. | `notebooks/analysis/10-correlation-classes.ipynb` computes class overlap/correlation and creates the population-weighted class-combination plot. |
| SF11 | Time evolution of percentage change in outflows by density and RDI category. | `notebooks/analysis/03-trend-extraction.ipynb` generates trend/time-series panels by origin category. |
| ST3 | Robustness of trend extraction methods. | `notebooks/analysis/03-trend-extraction.ipynb` produces the main trend extraction outputs used for comparison. |
| ST4 | Summary of model specifications. | Model definitions are implemented in `notebooks/analysis/05-trend-models.qmd` and `notebooks/analysis/08-city-trend-models.qmd`. |
| SF12 | Mixed-effects model estimates for old-age dependency categories. | `notebooks/analysis/05-trend-models.qmd` fits the old-age category models. `notebooks/analysis/06-recovery-times.ipynb` generates corresponding model/recovery panels. |
| ST5-ST10 | Country-level model result tables for outflows by density, RDI and old-age dependency categories. | `notebooks/analysis/05-trend-models.qmd` writes the tidy, glance and random-effects model outputs used to produce these tables. |
| ST11-ST22 | City-level model result tables for capital urban regions and FUAs. | `notebooks/analysis/08-city-trend-models.qmd` writes the city-level tidy, glance and random-effects model outputs used to produce these tables. |
| SF13 | Sensitivity of country-level model estimates to raw versus imputed movement data. | `notebooks/analysis/raw-sensitivity/05-raw-sensitivity-summary.ipynb` reads raw and imputed model outputs and produces comparison plots/tables. |
| SF14 | Sensitivity of city-level model estimates to raw versus imputed movement data. | `notebooks/analysis/raw-sensitivity/08-city-raw-sensitivity.ipynb` reads raw and imputed city-model outputs and produces comparison plots. |
| ST23-ST24 | Country-level recovery-time tables by density and RDI category. | `notebooks/analysis/05-trend-models.qmd` produces model outputs; `notebooks/analysis/06-recovery-times.ipynb` computes recovery-time estimates. |
| ST25-ST26 | City-level recovery-time tables for capital urban regions and FUAs. | `notebooks/analysis/08-city-trend-models.qmd` produces city-model outputs; `notebooks/analysis/09-city-recovery-times.ipynb` computes city-level recovery-time estimates. |


