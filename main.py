
import qrcode

class myQr:
    def __init__(self, size: int, padding:int):
        self.qr =qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=padding
        )
    def create_qr(self, file_name: str, fg:str,bg:str):
        user_input:str = input("Enter your website: ")



        try:
            self.qr.add_data(user_input)
            qr_image=self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Saved QR code to {file_name}')
        except Exception as e:
            print(f'Error:{e}')

def main():
    myqr = myQr(15,15)
    myqr.create_qr('qrcode.png','white','brown')


if __name__ == '__main__':
    main()


