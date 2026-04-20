# Workflow overview

This document provides an overview of the analysis workflow. It is intended to complement Figure 1 in the main manuscript by mapping each stage of the conceptual workflow to the corresponding notebooks in this repository.

The restricted Meta-Facebook input datasets are not distributed with the repository. With approved access to the data, the notebooks should be run in sequence, starting with preprocessing and then moving to the analysis notebooks.

## Workflow Stages

| Stage | Purpose | Main notebooks |
|---|---|---|
| 1. Spatial harmonisation | Assign consistent spatial identifiers to Facebook Population and Movement records so they can be linked across datasets and spatial layers. | `preprocessing/01-assign-FID-to-pop.ipynb`; `preprocessing/02-assign-FID-to-mov.ipynb` |
| 2. Baseline completion | Prepare complete baseline-period population and movement records used to define pre-pandemic reference levels. | `preprocessing/03-fill-baseline-pop.ipynb`; `preprocessing/04-fill-baseline-mov.ipynb` |
| 3. Population imputation | Impute missing or suppressed Facebook Population counts using WorldPop population estimates. | `preprocessing/05-impute-baseline-pop.ipynb` |
| 4. Spatial covariates | Aggregate baseline population information to movement tiles and add exogenous spatial variables, including population density, RDI and age-structure measures. | `preprocessing/06-aggregate-baseline-pop-to-mov.ipynb`; `preprocessing/07-add-exo-var-to-baseline-pop.ipynb` |
| 5. Movement imputation | Impute missing or suppressed Facebook Movement flows using the spatial interaction model. | `preprocessing/08-impute-baseline-mov.ipynb` |
| 6. Imputation summaries | Quantify the extent of missingness and imputation in the Facebook Population and Movement datasets. | `preprocessing/09-count-missing-values.ipynb` |
| 7. Descriptive evolution | Summarise population and mobility evolution across countries and spatial categories. | `analysis/01-pop-evolution.ipynb`; `analysis/02-mov-evolution.ipynb` |
| 8. Trend extraction | Create mobility trend series by country and category for the main modelling analysis. | `analysis/03-trend-extraction.ipynb` |
| 9. Descriptive before/after comparison | Produce before/after mobility comparisons for early-pandemic and later-period mobility levels. | `analysis/04-boxplots-before-after.ipynb` |
| 10. Country-level trend models | Fit country-level mixed-effects and GAM trend models for density, RDI and old-age dependency categories. | `analysis/05-trend-models.qmd` |
| 11. Country-level recovery times | Estimate recovery times from the country-level trend model outputs. | `analysis/06-recovery-times.ipynb` |
| 12. City and FUA netflows | Generate netflow time series for capital urban regions and all functional urban areas. | `analysis/07-mov-evolution-capital.ipynb` |
| 13. City-level trend models | Fit city/FUA mixed-effects and GAM trend models for netflows involving urban cores. | `analysis/08-city-trend-models.qmd` |
| 14. City-level recovery times | Estimate recovery times from city/FUA model outputs. | `analysis/09-city-recovery-times.ipynb` |
| 15. Category overlap | Examine overlap between population density and RDI classes. | `analysis/10-correlation-classes.ipynb` |
| 16. Raw-data sensitivity checks | Repeat selected trend extraction, descriptive comparison and model-output summaries using non-imputed/raw movement data. | `analysis/raw-sensitivity/` |

## Experimental branches

The main preprocessing workflow is in `notebooks/preprocessing/`. The folder `notebooks/preprocessing/builtup-experiments/` contains an experimental robustness branch that only imputes data in built-up areas. It is retained for transparency but is not required for the main analysis.

Older analysis notebooks that were retained for traceability are stored in `notebooks/analysis/superseded/`. These are not part of the current workflow.

## Figures and Tables

The relationship between manuscript figures and tables and the notebooks that generate their source outputs or panels is documented separately in `docs/figure-reproducibility.md`.

