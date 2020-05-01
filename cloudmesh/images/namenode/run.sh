#Referred https://github.com/big-data-europe/docker-hadoop/blob/master/namenode/run.sh

#!/bin/bash

namedir=`echo $HDFS_CONF_dfs_namenode_name_dir | perl -pe 's#file://##'`

#Checking whether the directory of the namenode is found
if [ ! -d $namedir ]; then
  echo "Namenode name directory not found: $namedir"
  exit 2
fi

#Checking whether the cluster name is specified or not
if [ -z "$CLUSTER_NAME" ]; then
  echo "Cluster name not specified"
  exit 2
fi

#Formatting the namenode directory
if [ "`ls -A $namedir`" == "" ]; then
  echo "Formatting namenode name directory: $namedir"
  #$HADOOP_PREFIX/bin/hdfs --config $HADOOP_CONF_DIR namenode -format $CLUSTER_NAME 
  hadoop namenode -format $CLUSTER_NAME
fi

$HADOOP_PREFIX/bin/hdfs --config $HADOOP_CONF_DIR namenode
