import subprocess
def install_modules(installer_mode="pip",options=""):
    with open("/home/jovyan/zeblokNotebooks/zeblokScripts/Modules.txt", 'r') as modules_file:
        modules = modules_file.readlines()
        for i,module in enumerate(modules):
            if(i==0):  print("============================================================================")
            command = installer_mode + " install " + module.strip() + " " + options
            print(str(i+1)+". Installing module- "+module.strip()+"\n")
            print(command)
            out,err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            if len(out)>0: print(out.decode('utf-8').strip()) 
            if len(err)>0: print("Error-\n"+err.decode('utf-8').strip())
            print("============================================================================")
        modules_file.close()
    return

# TODO uninstall_modules()

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    install_modules()