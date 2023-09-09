import sys



def main():
    #help/info
    if sys.argv[1] == "-h":
    	print("Usage: wrapper.py filetype visualisation path_to_file\n Filetypes: -pe -pcap \n Visualisations: -wordcloud -most-common")
    	sys.exit()
    
    #error if too many/ few arguments
    if len(sys.argv) != 4:
    	print("Incorrect usage: use wrapper.py -h for help")

    #define variables from cl arguments
    filetype = str(sys.argv[1])
    visualisation = str(sys.argv[2])
    path_to_file = str(sys.argv[3])

    #call scripts based on filetype and visualisation selected
    if (filetype == "-pe"):
        import pe_functions
        pe_functions.main(path_to_file, visualisation)

    elif (filetype == "-pcap"):
            return
            
    else: 
        print("Incorrect usage: use wrapper.py -h for help")
        sys.exit()



if __name__ == "__main__":
    main()
