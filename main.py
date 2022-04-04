#!/usr/bin/python

import sys
from node import Node


def start(n=2):
    nodes = []
    port = 8001
    host = "127.0.0.1"

    # Create the nodes
    for i in range(n):
        node = Node(host, port, id=f"P{i + 1}", n=n)
        port += 1
        node.start()
        nodes.append(node)

    # Connect the nodes
    for i in range(len(nodes)):
        node = nodes[i]
        for j in range(i + 1, len(nodes)):
            other_node = nodes[j]
            node.connect_with_node(host, other_node.port)

    while True:
        command = input("Enter command, press q to exit: \n")

        if command == "List":
            for node in nodes:
                print(node)
        elif "time-cs" in command:
            t = float(command.replace("time-cs ", ""))
            if t < 10:
                print("t must be larger than or equal to 10")
            else:
                for node in nodes:
                    node.time_cs = t
        elif "time-p" in command:
            t = float(command.replace("time-p ", ""))
            if t < 5:
                print("t must be larger than or equal to 5")
            else:
                for node in nodes:
                    node.time_p = t
        elif command == "q":
            break
        else:
            print("Unknown command")

    for node in nodes:
        node.stop()


start(int(sys.argv[1]))
