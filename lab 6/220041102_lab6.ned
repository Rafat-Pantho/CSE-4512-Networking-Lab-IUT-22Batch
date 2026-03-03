package inet.examples.ethernet.lans;

import inet.node.ethernet.EthernetHost;
import inet.node.ethernet.EthernetSwitch;
import ned.DatarateChannel;

network FiveLabs
{
    types:
        channel C extends DatarateChannel
        {
            delay = 0.1us;
            datarate = 100Mbps;
        }

    submodules:
        switch1: EthernetSwitch {
            parameters: @display("p=253,213");
            gates: ethg[4];
        }
        lab1hostA: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=273,109");
        }
        lab1hostB: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=153,213");
        }
        switch2: EthernetSwitch {
            parameters: @display("p=461,227");
            gates: ethg[4];
        }
        lab2hostA: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=443,117");
        }
        lab2hostB: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=353,213");
        }
        switch3: EthernetSwitch {
            parameters: @display("p=665,219");
            gates: ethg[4];
        }
        lab3hostA: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=653,150");
        }
        lab3hostB: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=565,217");
        }
        switch4: EthernetSwitch {
            parameters: @display("p=839,194");
            gates: ethg[4];
        }
        lab4hostA: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=853,107");
        }
        lab4hostB: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=757,209");
        }
        switch5: EthernetSwitch {
            parameters: @display("p=1127,214");
            gates: ethg[4];
        }
        lab5hostA: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=1057,104");
        }
        lab5hostB: EthernetHost {
            parameters:
                csmacdSupport = false;
                eth.duplexMode = true;
                @display("p=956,207");
        }

    connections:
        switch1.ethg[0] <--> C <--> lab1hostA.ethg;
        switch1.ethg[1] <--> C <--> lab1hostB.ethg;
        switch2.ethg[0] <--> C <--> lab2hostA.ethg;
        switch2.ethg[1] <--> C <--> lab2hostB.ethg;
        switch3.ethg[0] <--> C <--> lab3hostA.ethg;
        switch3.ethg[1] <--> C <--> lab3hostB.ethg;
        switch4.ethg[0] <--> C <--> lab4hostA.ethg;
        switch4.ethg[1] <--> C <--> lab4hostB.ethg;
        switch5.ethg[0] <--> C <--> lab5hostA.ethg;
        switch5.ethg[1] <--> C <--> lab5hostB.ethg;
        switch1.ethg[2] <--> C <--> switch2.ethg[2];
        switch2.ethg[3] <--> C <--> switch3.ethg[2];
        switch3.ethg[3] <--> C <--> switch4.ethg[2];
        switch4.ethg[3] <--> C <--> switch5.ethg[2];
}