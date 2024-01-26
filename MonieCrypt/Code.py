from click_shell import shell
import click
import SpecialPurpose as fn  


@shell(prompt= "\nMonieCrypt> ",intro = "to check the available commands , enter help.")
def MonieCrypt():
   fn.welcome()
    

@MonieCrypt.command()
def help():
    print("encryption -To encrypt a file ")
    print("decryption -To decrypt a file")
    print("frequency  -To d frequency analysis)")
    print("attack     -TO use frequency attack")
    print("cat        -Show file contents ")
    print("clear      -Clear terminal")
    print("\n")


@MonieCrypt.command()
def encryption():
    while True:
        option = input("Enter the option you want\n 1.Old Mono\n 2.New Mono\n >> ")
        
        if(option=="1"):
            infile = fn.readFile() 
            outfile = fn.writeFile(fn.oldEnc(fn.getKey(),infile))
            print(f"Done Successfully, the output is saved in {outfile}")
            break

        elif option=="2":
            infile = fn.readFile() 
            global c ,d, n 
            c ,d, n = fn.new_mono_enc(fn.getKey(),infile)
            outfile = fn.writeFile(str(c))
            print(f"Done Successfully, the output is saved in {outfile}")
            break
        else:
           print("Invalid option. Try again")

                                    

@MonieCrypt.command()
def decryption():
    while True:
        option = input("Enter the option you want\n 1.Old Mono\n 2.New Mono\n >>")
        if(option=="1"):
            infile = fn.readFile()
            outfile = fn.writeFile(fn.oldDec(fn.getKey(),infile))
            print(f"Done Successfully , the output is saved in {outfile}")
            break
        elif option=="2":
            infile =fn.readFile()
            outfile = fn.writeFile(fn.new_mono_dec(fn.getKey(),int(infile),d,n))
            break
        else:
           print("Invalid option. Try again")


@MonieCrypt.command()
@click.option('-n',help="gram size",required=1)
def frequency(n):
        infile = fn.readFile()
        if n=="1":
            freq_dict = fn.Unigram_frequencyAnalysis(infile)
            fn.plot_analysis(freq_dict)
        elif n=="2":
            freq_dict = fn.Bigram_frequencyAnalysis(infile)
            fn.table_analysis(freq_dict)
        elif n=="3":
            freq_dict = fn.Trigram_frequencyAnalysis(infile)
            fn.table_analysis(freq_dict)
        else:
            print("Not a valid gram size , try 1,2 or 3")
        


@MonieCrypt.command()
@click.option('-f',help="target filename",required=1)
def cat(f):
    try:
        file = open(f,"r")
        print(file.read())
    except:
        print("no such file ")

@MonieCrypt.command()
def attack():
        file = fn.readFile()
        fn.Attack(file)

@MonieCrypt.command()
def clear():
    click.clear()
    fn.welcome()


MonieCrypt()
