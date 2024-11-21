#! /usr/bin/env python

# Import packages
import os
import argparse
import subprocess
import numpy as np
from astropy.table import Table
from concurrent.futures import ThreadPoolExecutor


# Download product with rsync
def download_spectrum(extract,home_path, remote, password):
    """Download product from remote server."""

    # Product name
    field = extract['field'] 

    # Remote URL
    remote_url = f'{remote}/{field}/spectra'

    # Files
    id = 'id'
    files = [f'{field}_{str(extract[id]).zfill(5)}.1D.fits'] #'1D,'field'

    # Execute command
    for file in files:
        # Download command
        command = [
            'curl',
            '-u',
            f'outthere:{password}',
            '-o',
            f'data/{field}/{file}',
            f'{remote_url}/{file}',
        ]

        #if os.path.exists(f'data\\{field}\\{file}'):
        #    print(f'{file}exist')
        #    continue

        try:
            subprocess.run(command, check=True)
            print(f'\n download {file} downloaded \n')
        except subprocess.CalledProcessError as e:
            print(f'Failed to download {file}. Error: {e}')


# Main Function
def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('extracted', type=str, help='Path to extracted table')
    parser.add_argument(
        '--remote',
        type=str,
        help='Remote URL',
        default='http://outthere-mpia.org/s3/data',
    )
    parser.add_argument('--ncpu', type=int, default=1)
    args = parser.parse_args()

    # Prompt User for input
    #print('Enter the password to the remote server')
    password = ''

    # Load extracted
    extracted = Table.read(args.extracted)

    # Remote URL
    remote = args.remote

    # Number of CPUs
    ncpu = args.ncpu

    # Create directories
    home = os.getcwd()
    for field in np.unique(extracted['field']):
        os.makedirs(os.path.join(home,'data',f'{field}'), exist_ok=True)
        os.makedirs(os.path.join(home,'png',f'{field}'), exist_ok=True)

    # Multi-threaded download
    if ncpu > 1:
        with ThreadPoolExecutor(ncpu) as executor:
            executor.map(
                lambda e: download_spectrum(e, home, remote, password),
                extracted,
            )

    # Single-threaded download
    else:
        for extract in extracted:
            download_spectrum(extract, home, remote, password)


if __name__ == '__main__':
    main()
