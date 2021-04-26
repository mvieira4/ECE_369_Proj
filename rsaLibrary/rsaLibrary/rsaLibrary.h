#pragma once
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
}
