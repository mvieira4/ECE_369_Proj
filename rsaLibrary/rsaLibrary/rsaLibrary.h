#pragma once
namespace rsaLibrary
{
	class encryptedData			//class contains both the encrypted and unencrypted data
	{
	public:
		double encryptedValue;
		double decryptedValue;
	};

	class rsaClass
	{
	public:
		int gcd(int val1, int val2);

		encryptedData RSA(encryptedData input);

		double toAscii(char input);

		char toChar(double input);
	};
}
