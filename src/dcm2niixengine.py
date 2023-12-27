from utils import * 

def dcm2niix_convert(path, engine, kwargs):
        # check that dcm2niix is installed
        check_engine(engine)

        # check that all files are unzipped
        tgzunzip()

        # generate args
        a = get_kwargs(kwargs)
        if not a:
            bash = f'dcm2niix {path}'
        else:
            bash = f'dcm2niix {a} {path}'

        # execute
        subprocess.run(bash, shell=True, check=True, text=True)

        # update user
        process = subprocess.Popen(bash, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        status = process.poll()
        if status is not None:
            print(f'\noperation complete\n')