// StringStuff.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <stdio.h>
//#include <string.h>
#include <stdlib.h>
#include <string>
using namespace std;

int main()
{
	string stringArray[3], totel = "";
	char tmp[30];
	
	/*printf("wright stuff: ");
	scanf_s("%29s", tmp, _countof(tmp));//spaces do not work for this so insted i am using underscors
	stringArray[0] = tmp;
	scanf_s("%29s", tmp, _countof(tmp));//spaces do not work for this so insted i am using underscors
	stringArray[1] = tmp;
	scanf_s("%29s", tmp, _countof(tmp));//spaces do not work for this so insted i am using underscors
	stringArray[2] = tmp;
	//scanf_s("%s", &stringArray[1], stringArray[1].length);
	//scanf_s("%s", &stringArray[2]), stringArray[2].length;*/
	stringArray[0] = "this is the first messig";
	stringArray[1] = "this is the second messig";
	stringArray[2] = "this is the third messig";
	printf("%s, %s, %s", stringArray[0].c_str(), stringArray[1].c_str(), stringArray[2].c_str());
	for (string x : stringArray)
	{
		totel = totel + x + "\n";
	}
	//strcat_s(totel, first);
	//strcat_s(totel, "\n");
	//strcat_s(totel, second);
	//strcat_s(totel, "\n");
	//strcat_s(totel, third);
	printf("\n%s\n", totel.c_str());
	
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
