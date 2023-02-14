# GraphStateVis: Interactive Visual Analysis of Qubit Graph States and their Stabilizer Groups

## Prototype - Graphical User Interface

[![GraphStateVis](https://github.com/GraphStateVis/app/blob/main/figures/graphstatevis_components.png?raw=true)](https://graphstatevis.github.io/app)

## Abstract

Fathoming out quantum state space is a challenging endeavor due to its exponentially growing dimensionality. At the expense of being bound in its expressiveness, the discrete and finite subspace of graph states is easier to investigate via a pictorial framework accompanied with a theoretical toolkit from the stabilizer formalism. Analyzing hand-drawn graphs is a tedious and time-consuming task and imposes limitations to the problem sizes that can be addressed. Similarly, algorithmic studies using adjacency matrices alone lack the benefit of a visual representation of the states. We argue that applying visual analytics to investigate graph states can be advantageous. To this end, we introduce [GraphStateVis](https://graphstatevis.github.io/app), a web-based application for the visual analysis of qubit graph states and their stabilizer groups. Our tool facilitates the interactive construction of a graph through multiple components supported by linking and brushing. The user can explore graph-state-specific properties, including the Pauli-weight distribution of its stabilizer operators and noise thresholds for entanglement criteria. We propose a use case in the context of near-term quantum algorithms to illustrate the capabilities of our prototype. We provide access to [GraphStateVis](https://graphstatevis.github.io/app) as an open-source project and invite the broader quantum computing and engineering communities to take advantage of this tool and further boost its development.

## Description

[GraphStateVis](https://graphstatevis.github.io/app) is an application for the `Interactive Visual Analysis of Qubit Graph States and their Stabilizer Groups`

## Citing this paper

```bibtex
@inproceedings{miller2021graphstatevis,
  author    = {Matthias Miller and Daniel Miller},
  booktitle = {{IEEE} International Conference on Quantum Computing and Engineering ({QCE})},
  title     = {{GraphStateVis: Interactive Visual Analysis of Qubit Graph States and their Stabilizer Groups}}, 
  year      = {2021},
  pages     = {378--384},
  publisher = {{IEEE}},
  doi       = {10.1109/QCE52317.2021.00057}
}
```

## License
Released under MIT License. See the [LICENSE](LICENSE) file for details. The prototype was developed by Matthias Miller from the [Data Analysis and Visualization Group](https://www.vis.uni-konstanz.de/) at the University Konstanz.
