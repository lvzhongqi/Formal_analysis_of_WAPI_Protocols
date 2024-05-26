# Formal Analysis of WAPI Authentication and Key Agreement Protocol
This is the source code repo for the Formal Analysis of WAPI, a formal verification tool to analyze the WAPI Authentication and Key Agreement Protocol.  This instruction describes the organization of the source code and how to use it.


## Instructions

### Software Requirements
To run this Code, you need [ProVerif 2.01+](https://prosecco.gforge.inria.fr/personal/bblanche/proverif/ or use the version we has provided) and Python 3.0+ (to batch ProVerif input file.).

### File Organization

Source code files:
- /proverif: The ProVerif that we use and provide
- execute.py: Python file that runs all .pv files at once and calculates time consumption
- WAPI_Auth_initial.pv: Certificate-based Authentication initial Process to analyze confidentiality and authentication goals.
- WAPI_Auth_repeat.pv: Certificate-based Authentication repeat Process to analyze confidentiality and authentication goals.
- WAPI_Group.pv: Multicast Key agreement Process to analyze confidentiality and authentication goals
- WAPI_Unicast_repeat.pv: Unicast Key Update Process to analyze confidentiality and authentication goals
- WAPI_Unicast.pv: Initial Unicast Key Agreement Process to analyze confidentiality and authentication goals


### Verify the confidentiality and authentication goals
*With a large number of input cases, we use a python script to batch analyze (execute.py).
You can run the script without arguments and analyze confidentiality and authentication objectives in all cases.

```
PROJECTROOTDIR> python execute.py
```

Or you can run 'proverif ./' + filename to specific which process you want to analyze. 

```
PROJECTROOTDIR> proverif ./WAPI_Auth_initial.pv
```