# Balmer-decrement-JWST
Study Balmer decrement from JWST Outthere data

This project attempts to study spatially resolved balmer decrement from JWST-Outthere data.


The *work_flow* jupyter note book performs objects selection, downloading and extracting line maps from the existing data products of Outthere data sever. It also calculates PSFs for individual Ha Hb line maps as well as kernel to convolve hb psf to ha for acurate line maps

## package requirement

numpy; astropy; matplotlib; webbpsf; os; tqdm; gc; warnings; pathlib; photutils

## Current progress

Most primitive function is realized, incl. 

1. loading spectra
2. extract Ha Hb maps, error maps generated from line weight maps
3. monochromatic psf calculation; psf matching; error propagation
4. radial profile of balmer decrement

What can be done in the future:



[\\]:~~(!!!! just found) Position angle is not given in the final data product, it is recommended to average over PSFs of all possible possible angles in [this paper](https://doi.org/10.3847/2041-8213/ad28bd)~~ 

~~(+++) use weight map in the data products to generate variance map for error propagation~~

(+++) the result from balmer decrement radial needs optimization

(++)alternative method found? [Prospector SED fitting](https://arxiv.org/pdf/2404.17629)

(++) calculate theoretical galaxy mass using SED fitting from dense basis

(++)catalog crossmatching + mass catalog matching from 3D-HST for uma-03 field

(+) diagramm plot (e.g. balmer decrement, EW against mass SFR)

(+) Ha line maps rescaling to correct for NII line emission

