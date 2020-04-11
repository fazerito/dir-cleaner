import os
import sys
import shutil

if len(sys.argv) != 2:
    print('Wrong arguments')
    sys.exit()

else:
    try:
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf',
                            '.eps', '.ai', '.indd', '.raw', '.bmp', '.blend', '.dgn',
                            '.dwf', '.dwg', '.dxf', '.3ds')

        archive_extensions = ('.zip', '.rar', '.tar', '.tar.gz', '.iso', '.bz2', '.gz',
                              '.lz', '.rz', '.xz', '.s7z', '.7z', '.ark', '.b1', '.tgz',
                              '.tar.Z', '.tar.bz2', '.tbz2', '.tar.lz', '.tlz',
                              '.tar.xz', '.txz')

        docs_extensions = ('.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx', '.html',
                           '.htm', '.ods', '.ppt', '.pptx', '.txt', '.log', '.cfg',
                           '.ott', '.odm', '.ods', '.ots', '.csv')

        destination_dir = sys.argv[1]
        files = [file for file in os.listdir(destination_dir) 
                 if os.path.isfile(os.path.join(destination_dir, file))]

        for f in files:
            filename, file_extension = os.path.splitext(f)
            file_extension = file_extension.lower()
            if file_extension in image_extensions:
                if not os.path.exists(os.path.join(destination_dir, 'images')):
                    os.mkdir(os.path.join(destination_dir, 'images'))
                shutil.move(f'{destination_dir}/{f}', f'{destination_dir}/images/{f}')
                continue

            if file_extension in archive_extensions:
                if not os.path.exists(os.path.join(destination_dir, 'archives')):
                    os.mkdir(os.path.join(destination_dir, 'archives'))
                shutil.move(f'{destination_dir}/{f}', f'{destination_dir}/archives/{f}')
                continue

            if file_extension in docs_extensions:
                if not os.path.exists(os.path.join(destination_dir, 'docs')):
                    os.mkdir(os.path.join(destination_dir, 'docs'))
                shutil.move(f'{destination_dir}/{f}', f'{destination_dir}/docs/{f}')
                continue
            if '.exe' in file_extension:
                if not os.path.exists(os.path.join(destination_dir, 'exe')):
                    os.mkdir(os.path.join(destination_dir, 'exe'))
                shutil.move(f'{destination_dir}/{f}', f'{destination_dir}/exe/{f}')
                continue
    except Exception as ex:
        print(ex)
