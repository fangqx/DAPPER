# "Lorenz-95" (or 96) model. For a deeper introduction, see
# "DAPPER/tutorials/T4 - Dynamical systems, chaos, Lorenz.ipynb"
#
# Note: implementation is ndim-agnostic.

import numpy as np
from tools.math import rk4, integrate_TLM, is1d

Force = 8.0

# Note: the model is unstable (blows up) if there are large peaks
# (as may be occasioned by the analysis update, especially with partial obs). 
# Example: integrate 4 steps with dt=0.05 from x0 = [0,-30,0,30].
# This is effectively a CFL condition... Can be addressed by:
#  - lowering dt
#  - using an implicit time stepping scheme instead of rk4
#  - stupidly crop amplitudes, as is done here:
prevent_blow_up = False

def dxdt(x):
  a = x.ndim-1
  s = lambda x,n: np.roll(x,-n,axis=a)
  return (s(x,1)-s(x,-2))*s(x,-1) - x + Force

def step(x0, t, dt):

  if prevent_blow_up:
    clip      = abs(x0)>30
    x0[clip] *= 0.1

  return rk4(lambda t,x: dxdt(x), x0, np.nan, dt)


def TLM(x):
  """Tangent linear model"""
  assert is1d(x)
  m    = len(x)
  TLM  = np.zeros((m,m))
  md   = lambda i: np.mod(i,m)
  for i in range(m):
    TLM[i,i]       = -1.0
    TLM[i,   i-2 ] = -x[i-1]
    TLM[i,md(i+1)] = +x[i-1]
    TLM[i,   i-1 ] = x[md(i+1)]-x[i-2]
  return TLM

def dfdx(x,t,dt):
  """Integral of TLM. Jacobian of step."""
  # method='analytic' is a substantial upgrade for Lor95 
  return integrate_TLM(TLM(x),dt,method='analytic')



