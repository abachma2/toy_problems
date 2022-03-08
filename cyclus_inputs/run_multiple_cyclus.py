import json
import re
import subprocess
import os
import sqlite3 as lite
import copy
import glob
import sys
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import d3ploy.tester as tester
import d3ploy.plotter as plotter
import collections


# Delete previously generated files
direc = os.listdir('./')
hit_list = glob.glob('test_*.sqlite') #+ glob.glob('*.json') + \
    #glob.glob('*.png') + glob.glob('*.csv') + glob.glob('*.txt')
for file in hit_list:
    os.remove(file)

ENV = dict(os.environ)
ENV['PYTHONPATH'] = ".:" + ENV.get('PYTHONPATH', '')


##### List of types of calc methods that are to be tested #####
calc_methods = ["ma", "arma", "arch", "poly",
                "exp_smoothing", "holt_winters", "fft", "sw_seasonal"]

scenario_template = {
    "simulation": {
        "archetypes": {
            "spec": [
                    {"lib": "agents", "name": "NullRegion"},
                    {"lib": "cycamore", "name": "Source"},
                    {"lib": "cycamore", "name": "Reactor"},
                    {"lib": "cycamore", "name": "Sink"},
                    {"lib": "d3ploy.demand_driven_deployment_inst", "name": "DemandDrivenDeploymentInst"}
            ]
        },
        "control": {"duration": "100", "startmonth": "1", "startyear": "2000"},
        "recipe": [
            {
                "basis": "mass",
                "name": "fresh_uox",
                "nuclide": [{"comp": "0.711", "id": "U235"}, {"comp": "99.289", "id": "U238"}]
            },
            {
                "basis": "mass",
                "name": "spent_uox",
                "nuclide": [{"comp": "50", "id": "Kr85"}, {"comp": "50", "id": "Cs137"}]
            }
        ]}}


scenario_input = {}
demand_eq = "np.heaviside(t-500,0.5)*300"

for calc_method in calc_methods:
    scenario_input[calc_method] = copy.deepcopy(scenario_template)
    scenario_input[calc_method]["simulation"].update({"facility": [{
        "config": {"Source": {"outcommod": "fuel",
                              "outrecipe": "fresh_uox",
                              "throughput": "3000"}},
        "name": "source"
    },
        {
        "config": {"Sink": {"in_commods": {"val": "spentfuel"},
                            "max_inv_size": "1e6"}},
        "name": "sink"
    },
        {
        "config": {
            "Reactor": {
                "assem_size": "1000",
                "cycle_time": "1",
                "fuel_incommods": {"val": "fuel"},
                "fuel_inrecipes": {"val": "fresh_uox"},
                "fuel_outcommods": {"val": "spentfuel"},
                "fuel_outrecipes": {"val": "spent_uox"},
                "n_assem_batch": "1",
                "n_assem_core": "3",
                "power_cap": "1000",
                "refuel_time": "0",
            }
        },
        "name": "reactor"
    }]})
    scenario_input[calc_method]["simulation"].update({"region": {
        "config": {"NullRegion": "\n      "},
        "institution": {
            "config": {
                "DemandDrivenDeploymentInst": {
                    "calc_method": calc_method,
                    "facility_commod": {
                        "item": [
                            {"commod": "fuel", "facility": "source"},
                            {"commod": "POWER", "facility": "reactor"}
                        ]
                    },
                    "facility_capacity": {
                        "item": [
                            {"capacity": "3000", "facility": "source"},
                            {"capacity": "1000", "facility": "reactor"}
                        ]
                    },
                    "driving_commod": "POWER",
                    "demand_eq": demand_eq,
                    "record": "1",
                    "steps": "1"
                }
            },
            "name": "source_inst"
        },
        "name": "SingleRegion"
    }})

metric_dict = {}

for calc_method in calc_methods:
    name = "test_input_" + calc_method
    input_file = name + ".json"
    output_file = name + ".sqlite"
    with open(input_file, 'w') as f:
        json.dump(scenario_input[calc_method], f)

    s = subprocess.check_output(['cyclus', '-o', output_file, input_file],
                                universal_newlines=True, env=ENV)