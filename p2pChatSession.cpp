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

    public:
        p2pChatSession()
        {
            printf("[*] Waiting For Inbound Connection...");
        }

        void requeP2p(int targetPort)
        {
            int sendPipe = socket(AF_INET, SOCK_STREAM, 0);
            int recvPipe = socket(AF_INET, SOCK_STREAM, 0);

            struct sockaddr_in targetAddress;
            targetAddress.sin_family = AF_INET;
            targetAddress.sin_port = htons(targetPort);
            targetAddress.sin_addr.s_addr = INADDR_ANY;

            connect(sendPipe, (struct sockaddr *)&targetAddress, sizeof(targetAddress));
        }
};