# Balmer-decrement-JWST
Study Balmer decrement from JWST Outthere data

This project attempts to study spatially resolved balmer decrement from JWST-Outthere data.


The *work_flow* jupyter note book performs objects selection, downloading and extracting line maps from the existing data products of Outthere data sever. It also calculates PSFs for individual Ha Hb line maps as well as kernel to convolve hb psf to ha for acurate line maps

## package requirement

numpy; astropy; matplotlib; webbpsf; os; tqdm; gc; warnings; pathlib; photutils


## Current progress

Most primitive function is realized, incl. 

loading spectra, extract Ha Hb maps, monochromatic psf calculation, matching psf calculation.

What can be done in the future:

(+++) use weight map in the data products to generate variance map for error propagation

(++) calculate galaxy mass using SED fitting from dense basis

(++) diagramm plot (e.g. balmer decrement, EW against mass SFR)

(+) Ha line maps rescaling to correct for NII line emission

