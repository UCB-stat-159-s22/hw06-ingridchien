## Fine-tuning reproduciblity of LIGO Black Hole signal tutorial, Part II

**Note:** This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original analysis code rests with the LIGO collaboration.

**Makefile Targets:** 

`env`: creates and configures the environment.

`html`: build the JupyterBook normally (calling jupyterbook build .). Note this build can only be viewed if the repo is cloned locally, or with the VNC desktop on the hub.

`html-hub`: build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above.

`clean`: clean up the figures, audio and _build folders.

**Activating the Environment:**

Activate the installed environemnt with `conda activate ligo`. Utilize pytests and the ligotools package in the ligo environment. 

**Ligotools Test:**

Use `pytest ligotools` in the ligo environment to run package tests. 

**Building the Jupyter Book:**

If you are in the ligo environment, Deactivate the ligo deactivate with `conda deactivate` before running the makefile targets that build the jupyter book. 

If you are working on the hub, visit the following link after running the `hmtl-hub` makefile target to view the book.

https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html