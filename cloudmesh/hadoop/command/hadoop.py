from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.cluster.Cluster import Cluster
from cloudmesh.common.Printer import Printer
class HadoopCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_hadoop(self, args, arguments):
        """
        ::

          Usage:
                hadoop [LABEL]

          Deploys hadoop on a cloud cluster.

          Arguments:
              LABEL   A cluster label.

          Description:
              
              hadoop [LABEL]

                  Deploy hadoop onto a cluster.  Automatically determines master and client nodes.  If cluster name not specified, 
                  cluster is created automatically.
        """
        VERBOSE(arguments)

        map_parameters(arguments, LABEL)
        
        cluster = Cluster(printer=Printer.write, name=arguments.cloud)
        if arguments.LABEL:
            cluster.deploy("../images/")

        return ""
