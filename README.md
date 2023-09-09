#  📈 MalViz

## Wrapper script:
Calls other scripts based on command line arguments.

Usage: ```wrapper.py filetype visualisation path_to_file``` Filetypes: ```-pe``` ```-pcap```  Visualisations: ```-wordcloud``` ```-most-common```

Example: ```python3 wrapper.py -pe -most-common 1.exe```

<img src="https://i.ibb.co/LQ7fq7v/Screenshot-Kali-2023-09-09-12-18-31.png" width="70%">

<hr>

# 🔨 TODO:
1. Integrate more visualisation scripts
2. Exception handling and logging
3. Option to write visualisations to file (plt.savefig)
4. Optimise Python import calls
5. Rewrite wrapper.py as GUI or compiled
6. Streamline application install
