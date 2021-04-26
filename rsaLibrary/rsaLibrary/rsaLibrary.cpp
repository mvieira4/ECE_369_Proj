/*#include <stdio.h>
#include<math.h>
#include "rsaLibrary.h"
//Program is intended to generate an rsa key using the public and private keys
//idea is to have the message converted into either a string or series of chars, translate the value into its ascii value, and then encrypt it here
/*class encryptedData			//class contains both the encrypted and unencrypted data
{
public:
	double encryptedValue;
	double decryptedValue;
};
namespace rsaLibrary
{

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

	double rsaClass:: RSA(encryptedData input, int identifier) //unencrypted is the ascii value of the input char, identifier tells if we are encrypting(1) or decrypting(anything other than 1)
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

	double rsaClass:: toAscii(char input)
	{
		double ascii;
		ascii = double(input);
		return ascii;
	}
	char rsaClass :: toChar(double input)
	{
		double character;
		character = char(input);
		return character;
	}
}
*/
//library file reference:  https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160
//TO TEST: CREATE A CPP FILE AND PASTE THE FOLLOWING
/*

#include <stdio.h>
#include<math.h>
#include "RSA.h"


void main()		//used for debugging, not needed in project application of code, provides an example of how the encryption is to be used
{
	char rawInput, decryptionTestChar;
	double  encryptionTest, decryptionTestAscii;
	encryptedData asciiTest;
	int identifier, identifier2;
	rawInput = 'h';			//input character from the string we are encrypting
	asciiTest.decryptedValue = toAscii(rawInput);		//convert to ascii
	asciiTest.encryptedValue = -1;						//not needed necessarily, just done for initialization/safety
	printf("Character input = %c\n", rawInput);
	printf("Ascii converter = %lf\n", asciiTest.decryptedValue);	//demonstrate toAscii
	identifier = 1;
	asciiTest.encryptedValue = RSA(asciiTest, identifier);										//data encrypted here, saves both encrypted and unencrypted data to asciiTest
	encryptionTest = asciiTest.encryptedValue;
	printf("RSA encryption function returns: %lf\n", encryptionTest);	//test encryption functionality (print this if you want to show the encrypted data)
	identifier2 = 0;
	asciiTest.encryptedValue = RSA(asciiTest, identifier2);
	decryptionTestAscii = asciiTest.decryptedValue;
	printf("RSA decryption function returns: %lf\n", decryptionTestAscii);	//test decryption functionality (print this if you want to show the decrypted data in number form)
	decryptionTestChar = toChar(decryptionTestAscii);
	printf("Decryption Character input = %c\n", decryptionTestChar);		//test toChar function  (print the toChar of the input.decryptedValue property to display the decrypted character)
	return;
}*/