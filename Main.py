import qrcode

def gerar_qrcode():
    dado = input("Digite o texto ou link para gerar o QR Code: ")
    imagem_qr = qrcode.make(dado)
    imagem_qr.save("qrcode_gerado.png")
    print("QR Code gerado e salvo como 'qrcode_gerado.png'.")

if __name__ == "__main__":
    gerar_qrcode()
