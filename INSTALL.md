```
sudo apt-get update
sudo apt-get install -y gcc
sudo apt-get install -y make
sudo apt-get install -y libbz2-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y libncurses5-dev 
sudo apt-get install -y libncursesw5-dev
sudo apt-get install -y liblzma-dev
pip3 install matplotlib

# create and activate conda env
conda create --name env1
conda activate env1

# SRA Toolkit (if forward and reverse are in same file and need to be separated)
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.8/sratoolkit.2.10.8-ubuntu64.tar.gz
tar -C /path/to/project/directory -zxvf sratoolkit.2.10.8-ubuntu64.tar.gz
cd path/to/sratoolkit.2.10.8-ubuntu64/bin
./vdb-config -i 
# press "tab" and exit to accept defaults
# /home/user/ncbi/public will be location of user-repository

# BWA (Burrows-Wheeler Aligner)
sudo apt install bwa

# samtools
cd /usr
sudo wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
sudo tar -C /usr/bin -vxjf samtools-1.9.tar.bz2
cd /usr/bin/samtools-1.9
sudo make
export PATH="$PATH:/usr/bin/samtools-1.9"
source ~/.profile

# bedtools
sudo apt install bedops

# EFetch for NCBI sequences
wget --user-agent="Mozilla" https://www.ncbi.nlm.nih.gov/books/NBK179288/bin/install-edirect.sh
source ./install-edirect.sh

# downloadfiles for this example
# HIV genome reference: K03455.1
esearch -db nucleotide -query "K03455.1" | efetch -format fasta > K03455.1.fasta

# MiSeq data set
wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos1/sra-pub-run-5/SRR961514/SRR961514.1
# extract forward and reverse from MiSeq data set
fastq-dump --split-files SRR961514.1
# Result: forward: SRR961514.1_1.fastq, reverse: SRR961514.1_2.fastq 
```


