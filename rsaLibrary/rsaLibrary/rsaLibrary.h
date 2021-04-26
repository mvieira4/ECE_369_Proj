//library file reference:  https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160
#pragma once
#include <stdio.h>
#include<math.h>
#include "rsaLibrary.h"

namespace rsaLibrary
{
	class encryptedData			//class contains both the encrypted and unencrypted data
	{
	public:
		double encryptedValue;
		double decryptedValue;
		double encryptedValueUnmodded;
	};

	class rsaClass
	{
	public:
		int gcd(int val1, int val2);

		double RSA(encryptedData input, int identifier);

		double toAscii(char input);

		char toChar(double input);
	};
	int rsaClass::gcd(int val1, int val2) //method/function finds the greatest common denominator
	{
		int modCheck;
		while (true)
		{
			modCheck = val1 % val2;
			if (modCheck == 0)
			{
				return val2;
			}
			val1 = val2;
			val2 = modCheck;
		}
	}

	double rsaClass::RSA(encryptedData input, int identifier) //unencrypted is the ascii value of the input char, identifier tells if we are encrypting(1) or decrypting(anything other than 1)
	{
		double p, q, n, ePublic, phi, ePrivate, ePrivateTemp;	//p, q are random numbers and can be changed, n and phi is based on p, ePublic is used for public encryption key
		int gcdTest;	 // ePrivate and ePrivateTemp are used in generating a private key, gcdTest is based on gcd method
		p = 17;	//any prime #
		q = 3;	//any prime #
		ePublic = 47;	//prime number
		n = q * p;
		phi = (p - 1)*(q - 1);
		while (ePublic < phi)
		{
			gcdTest = gcd(ePublic, phi);
			if (ePublic == 1)
				break;
			else
				ePublic++;
		}
		ePrivateTemp = 1 / ePublic;		//ePrivate must satisfy condition of ePrivate*ePublic = 1 % phi
		ePrivate = fmod(ePrivateTemp, phi);
		if (identifier == 1)
		{
			input.encryptedValueUnmodded = pow(input.decryptedValue, ePublic);		//encryption keys are generated here
			input.encryptedValue = fmod(input.encryptedValueUnmodded, n);					//encrypted data defined
			return input.encryptedValue;
		}
		else
		{
			input.decryptedValue = round(pow(input.encryptedValueUnmodded, ePrivate));		//decrypted data defined
			return input.decryptedValue;
		}
	}

	double rsaClass::toAscii(char input)
	{
		double ascii;
		ascii = double(input);
		return ascii;
	}
	char rsaClass::toChar(double input)
	{
		double character;
		character = char(input);
		return character;
	}
}
