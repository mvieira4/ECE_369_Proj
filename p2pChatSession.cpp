#include <stdio.h>
#include <thread>
#include <time.h>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <WinSock2.h>

using namespace std;

class p2pChatSession
{
    queue<string> messageQueue;

    queue<string> sendQueue;

    vector<vector <int>> connectionList;

    int active = 1;

    public:
        p2pChatSession()
        {
            printf("[*] Waiting For Inbound Connection...");
        }

        void requeP2p(int targetPort)
        {
            struct sockaddr_in targetAddress;
            targetAddress.sin_family = AF_INET;
            targetAddress.sin_port = htons(targetPort);
            targetAddress.sin_addr.s_addr = INADDR_ANY;

            int sendPipe = socket(AF_INET, SOCK_STREAM, 0);
            connect(sendPipe, (struct sockaddr *)&targetAddress, sizeof(targetAddress));
            std::cout << "[i] Created Sending Pipeline";

            int recvPipe = socket(AF_INET, SOCK_STREAM, 0);
            connect(recvPipe, (struct sockaddr *)&targetAddress, sizeof(targetAddress));
            std::cout << "[i] Created Receiving Pipeline";

            vector<int> connection {recvPipe, sendPipe};
            connectionList.insert(connectionList.end(), connection);
        }

        void acptP2p()
        {
            while(active)
            {
                int rec
            }
        }
};