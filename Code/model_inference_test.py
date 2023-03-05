from deepmd.infer import DeepPot
import numpy as np
import dpdata
import os
import pandas as pd

def get_systems(path):
    result = []
    energy_ground_truth = []
    force_ground_truth = []
    for s in os.listdir(path):
        energy = np.load(os.path.join(path,s) +'/set.000/energy.npy')
        force = np.load(os.path.join(path,s) +'/set.000/force.npy')
        energy_ground_truth.extend(energy)
        force_ground_truth.extend(force)
        result.append(dpdata.LabeledSystem(os.path.join(path, s), fmt='deepmd/npy'))
    return result,energy_ground_truth,force_ground_truth

if __name__ == '__main__':
    systems,energy_ground_truth,force_ground_truth = get_systems('../../data/water/ice_pimd/test')
    energy_prediction = []
    force_prediction = []
    data_points = []
    dp = DeepPot('graph-compress.pb')
     
    ##Prediction
    for sys in systems:
        nframes = sys['coords'].shape[0]
        coords = sys['coords']
        cells = sys['cells']
        atom_types = sys['atom_types']

        for idx in range(nframes):
            coord = coords[idx].reshape([1,-1])
            cell = cells[idx].reshape([1,-1])
            e,f,v = dp.eval(coord,cell,atom_types)
            energy_prediction.append(e[0][0])
            force_prediction.append(f[0][0])

    ##Creating DataFrame
    df = pd.DataFrame(columns=['energy_ground_truth','force_ground_truth','energy_predictions','force_predictions'])
    df['energy_ground_truth'] = energy_ground_truth
    df['force_ground_truth'] = force_ground_truth
    df['energy_predictions'] = energy_prediction
    df['force_predictions'] = force_prediction
    df.to_csv('../model_output_test_comparison.csv')
