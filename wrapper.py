import sys

main():
    if sys.argv[1] == "-h":
    	print("Usage: wrapper.py filetype visualisation path_to_file\n Filetypes: -pe -pcap \n Visualisations: -wordcloud -other")
    	sys.exit()
    
    #error if too many/ few arguments
    if len(sys.argv) != 4:
    	print("Incorrect usage: use wrapper.py -h for help")
    
    filetype = str(sys.argv[1])
    visualisation = str(sys.argv[2])
    path_to_file = str(sys.argv[3])
    
    if (filetype == "-pe"):
        if (visualisation == "-wordcloud"):
            import pe_wordcloud
            pe_wordcloud.main(path_to_file)
    
        elif (visualisation == "-other"):
            pass

    if (filetype == "-pcap"):
            pass
            
    else: 
        print("Incorrect usage: use wrapper.py -h for help")
        sys.exit()

if __name__ == "__main__":
    main()