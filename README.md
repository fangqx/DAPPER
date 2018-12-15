This (git) branch of DAPPER provides scripts to reproduce results from the article


    "Adaptive covariance inflation in the ensemble Kalman filter by Gaussian scale mixtures"
    by Patrick N. Raanes, Marc Bocquet, and Alberto Carrassi.


The results are given by `Figure 4 (a,b,c,d)`, which plot a table of
accuracy benchmarks of the various filters as functions of various control variables.

The scripts are located in the folder `AdInf` (which only exists on this git branch).
The scripts depend on the underlying package: DAPPER.
In particular, all of the `AdInf` scripts are based on `DAPPER/example_3.py`;
refer to this for more detailed commenting.
