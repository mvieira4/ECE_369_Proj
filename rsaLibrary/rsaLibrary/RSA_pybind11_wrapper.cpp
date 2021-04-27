#include <stdio.h>
#include <pybind11/pybind11.h>
#include "rsaLibrary.h"

PYBIND11_MODULE(rsaBind, m) {
	m.def("gcd", &gcd, "A function that finds the greatest common denomenator");
	m.def("RSA", &RSA, "A function that generates an rsa key and encyrpts/decrypts raw ascii data");
	m.def("toAscii", &toAscii, "A function that converts a char input to an ascii double");
	m.def("toChar", &toChar, "A function that converts a char input to an ascii double");
}

//try the following (or something similar) if the above does not work
/*
PYBIND11_MODULE(rsaBind, n) {
	n.def("gcd", &gcd, "A function that finds the greatest common denomenator");
}

PYBIND11_MODULE(rsaBind, o) {
	o.def("RSA", &RSA, "A function that generates an rsa key and encyrpts/decrypts raw ascii data");
}

PYBIND11_MODULE(rsaBind, p) {
	p.def("toAscii", &toAscii, "A function that converts a char input to an ascii double");
}

PYBIND11_MODULE(rsaBind, q) {
	q.def("toChar", &toChar, "A function that converts a char input to an ascii double");
}
*/