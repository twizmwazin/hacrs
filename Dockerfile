FROM python:3.7.4
MAINTAINER Tariq M Nasim <tnasim@asu.edu>

# Create the group and user to be used in this container
RUN groupadd hacrsgroup && useradd -m -g hacrsgroup -s /bin/bash hacrs

# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/hacrs/app/
WORKDIR /home/hacrs/app/

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /home/hacrs/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /home/hacrs/app/

RUN chown -R hacrs:hacrsgroup /home/hacrs

USER hacrs
