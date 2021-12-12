#include <iostream>
#include <iomanip>
#include "..\cryptopp860\modes.h"
#include "..\cryptopp860\rsa.h"
#include "..\cryptopp860\des.h"
#include "..\cryptopp860\aes.h"
#include "..\cryptopp860\filters.h"
#include "..\cryptopp860\osrng.h"
using namespace std;
using namespace CryptoPP;

// Hansal Shah - 19BCP043 (Using Crypto++ library)

Integer n("0xbeaadb3d839f3b5f"), e("0x11"), d("0x21a5ae37b9959db9");
RSA::PrivateKey privKey;
RSA::PublicKey pubKey;
Integer encrypted_integer_rsa;

SecByteBlock key_des(0x00, DES_EDE2::DEFAULT_KEYLENGTH);
byte iv_des[DES_EDE2::BLOCKSIZE];

byte key_aes[AES::DEFAULT_KEYLENGTH], iv_aes[AES::BLOCKSIZE];

string encrypt_rsa(string message) {
    string ciphertext;

    Integer m((const byte*)message.data(), message.size());
    Integer c = pubKey.ApplyFunction(m);
    encrypted_integer_rsa = c;

    size_t req = c.MinEncodedSize();
    ciphertext.resize(req);

    c.Encode((byte*)&ciphertext[0], ciphertext.size());
    cout << "Ciphertext from RSA encryption: " << ciphertext << endl;

    return ciphertext;
}

string decrypt_rsa(string ciphertext) {
    AutoSeededRandomPool prng;
    string message;

    Integer c((const byte*)ciphertext.data(), ciphertext.size());
    Integer m = privKey.CalculateInverse(prng, c);

    size_t temp = m.MinEncodedSize();
    message.resize(temp);
    m.Encode((byte*)&message[0], message.size());
    cout << "Plaintext from RSA decryption: " << message << endl;
    return message;
}

string encrypt_des(string message) {
    string ciphertext;
    try
    {

        CBC_Mode< DES_EDE2 >::Encryption e;
        e.SetKeyWithIV(key_des, key_des.size(), iv_des);

        StringSource ss1(message, true,
            new StreamTransformationFilter(e,
                new StringSink(ciphertext)
            )
        );

        cout << "Ciphertext from DES encryption: " << ciphertext << endl;
        return ciphertext;
    }
    catch (const CryptoPP::Exception& e)
    {
        cerr << e.what() << endl;
        exit(1);
    }
}

string decrypt_des(string ciphertext) {
    string message;
    try
    {
        CBC_Mode< DES_EDE2 >::Decryption d;
        d.SetKeyWithIV(key_des, key_des.size(), iv_des);

        StringSource ss3(ciphertext, true,
            new StreamTransformationFilter(d,
                new StringSink(message)
            )
        );

        cout << "Plaintext from DES decryption: " << message << endl;
        return message;
    }
    catch (const CryptoPP::Exception& e)
    {
        cerr << e.what() << endl;
        exit(1);
    }
}

string encrypt_aes(string message) {
    string ciphertext;
    AES::Encryption aesEncryption(key_aes, AES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Encryption cbcEncryption(aesEncryption, iv_aes);

    StreamTransformationFilter stfEncryptor(cbcEncryption, new StringSink(ciphertext));
    stfEncryptor.Put(reinterpret_cast<const unsigned char*>(message.c_str()), message.length());
    stfEncryptor.MessageEnd();

    cout << "Ciphertext from AES encryption: " << ciphertext << endl;
    return ciphertext;
}

string decrypt_aes(string ciphertext) {
    string message;
    AES::Decryption aesDecryption(key_aes, AES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Decryption cbcDecryption(aesDecryption, iv_aes);

    StreamTransformationFilter stfDecryptor(cbcDecryption, new StringSink(message));
    stfDecryptor.Put(reinterpret_cast<const unsigned char*>(ciphertext.c_str()), ciphertext.size());

    cout << "Plaintext from AES decryption: " << message << endl;
    return message;
}



int main(int argc, char* argv[]) {
    AutoSeededRandomPool prng;

    // Initializing parameters for RSA crytography
    privKey.Initialize(n, e, d);
    pubKey.Initialize(n, e);

    // Initializing parameters for DES crytography
    prng.GenerateBlock(key_des, key_des.size());
    prng.GenerateBlock(iv_des, sizeof(iv_des));

    // Initializing parameter for AES cryptography
    memset(key_aes, 0x00, AES::DEFAULT_KEYLENGTH);
    memset(iv_aes, 0x00, AES::BLOCKSIZE);

    string message; cout << "Enter some text: "; cin >> message;

    // RSA Encryption
    string c1 = encrypt_rsa(message);

    // DES encryption
    string c2 = encrypt_des(c1);

    // AES encryption
    string c3 = encrypt_aes(c2);

    // AES decryption
    string c4 = decrypt_aes(c3);

    // DES decryption
    string c5 = decrypt_des(c4);

    // RSA decryption 
    string c6 = decrypt_rsa(c5);
}