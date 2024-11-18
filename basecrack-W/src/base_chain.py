import anybase32
import base36
import base45
import base58
import base62
import base64
import base91
import src.base92 as base92
import pybase100
from src.z85_decoder import z85_decode

from termcolor import colored

class DecodeBase:
    def __init__(self, encoded_base, api_call=False, image_mode=False):
        self.encoded_base = encoded_base
        self.b32_once = False
        self.b64_once = False
        self.b64_url = False
        self.encoding_type = []
        self.results = []

        # 状态条件
        self.api_call = api_call
        self.image_mode_call = image_mode

    def decode(self):
        self.decode_base()
        return (
            self.encoding_type,
            self.results
        )

    def contains_replacement_char(self, res):
        if u'\ufffd' in res:
            return True
        else:
            count = 0
            for char in res:
                if ord(char) > 127:
                    count += 1
            return True if count > 0 else False

    def process_decode(self, decode_string, scheme):
        encoding_type = self.encoding_type
        results = self.results

        if len(decode_string) < 3:
            return
        if not self.contains_replacement_char(decode_string):
            if scheme == 'Base64' and '://' not in decode_string:
                self.b64_once = True

            if self.b64_once and (scheme == 'Base64URL'):
                return

            encoding_type.append(scheme)
            results.append(decode_string)

            if not self.api_call:
                if self.image_mode_call:
                    print(
                        colored('\n[-] 尝试 Base: ', 'yellow') +
                        colored(self.encoded_base, 'red')
                    )

                print(
                    colored('\n[>] 以 {} 解码: '.format(scheme), 'blue') +
                    colored(decode_string, 'green')
                )

    def decode_base(self):
        encoded_base = self.encoded_base
        process_decode = self.process_decode

        # 尝试Base128解码
        try:
            decoded_num = int(encoded_base, 128)
            decoded_bytes = decoded_num.to_bytes((decoded_num.bit_length() + 7) // 8, 'big')
            decoded_string = decoded_bytes.decode('utf-8', 'replace')

            # 确保解码结果合理
            if len(decoded_string) > 0 and decoded_string != self.encoded_base:
                process_decode(decoded_string, 'Base128')
                return  # 如果成功解码，直接返回
        except Exception:
            pass

        # 尝试Base16解码
        try:
            decoded_bytes = base64.b16decode(encoded_base, casefold=False)
            if len(decoded_bytes) < len(encoded_base) // 2:  # 只有在解码结果长度小于输入长度的一半时才继续
                process_decode(decoded_bytes.decode('utf-8', 'replace'), 'Base16')
        except Exception:
            pass

        # 尝试Base32解码
        try:
            process_decode(
                base64.b32decode(encoded_base, casefold=False, map01=None).decode('utf-8', 'replace'),
                'Base32'
            )
            self.b32_once = True
        except Exception:
            pass

        # 尝试Base32hex解码
        try:
            base32hex_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
            base32_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
            translation_table = str.maketrans(base32hex_chars, base32_chars)
            translated_base = encoded_base.translate(translation_table)
            padding_length = (8 - len(translated_base) % 8) % 8
            translated_base += "=" * padding_length
            decoded = base64.b32decode(translated_base, casefold=True)
            process_decode(decoded.decode('utf-8', 'replace'), 'Base32hex')
        except Exception:
            pass

        # 尝试Base38解码
        try:
            base38_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-."
            decoded_num = 0

            for char in encoded_base:
                decoded_num = decoded_num * 38 + base38_chars.index(char)

            decoded_bytes = bytearray()
            while decoded_num > 0:
                decoded_bytes.append(decoded_num % 256)
                decoded_num //= 256
            
            decoded_bytes.reverse()
            process_decode(decoded_bytes.decode('utf-8', 'replace'), 'Base38')
        except Exception:
            pass

        # 尝试Base45解码
        try:
            process_decode(
                base45.b45decode(encoded_base).decode('utf-8', 'replace'),
                'Base45'
            )
        except Exception:
            pass

        # 尝试Base58解码
        try:
            process_decode(
                base58.b58decode(encoded_base.encode()).decode('utf-8', 'replace'),
                'Base58'
            )
        except Exception:
            pass

        # 尝试Base62解码
        try:
            process_decode(
                base62.decodebytes(encoded_base).decode('utf-8', 'replace'),
                'Base62'
            )
        except Exception:
            pass

        # 尝试Base64解码
        try:
            process_decode(
                base64.b64decode(encoded_base).decode('utf-8', 'replace'),
                'Base64'
            )
        except Exception:
            pass

        # 尝试Base64URL解码
        try:
            process_decode(
                base64.urlsafe_b64decode(
                    encoded_base + '=' * (4 - len(encoded_base) % 4)
                ).decode('utf-8', 'replace'),
                'Base64URL'
            )
        except Exception:
            pass

        # 尝试Base85解码
        try:
            process_decode(
                base64.b85decode(encoded_base).decode('utf-8', 'replace'),
                'Base85'
            )
        except Exception:
            pass

        # 尝试Ascii85解码
        try:
            process_decode(
                base64.a85decode(encoded_base).decode('utf-8', 'replace'),
                'Ascii85'
            )
        except Exception:
            pass

        # 尝试Base91解码
        try:
            process_decode(
                base91.decode(encoded_base).decode('utf-8', 'replace'),
                'Base91'
            )
        except Exception:
            pass

        # 尝试Base92解码
        try:
            process_decode(
                base92.decode(encoded_base),
                'Base92'
            )
        except Exception:
            pass

        # 尝试Base100解码
        try:
            process_decode(
                pybase100.decode(encoded_base).decode(),
                'Base100'
            )
        except Exception:
            pass

        # 尝试Z85解码
        try:
            process_decode(
                z85_decode(encoded_base).decode('utf-8', 'replace'),
                'Z85'
            )
        except Exception:
            pass

        # 尝试Base32z解码
        try:
            base32z_chars = "ybndrfg8ejkmcpqxot1uwisza345h769"
            standard_base32_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
            translation_table = str.maketrans(base32z_chars, standard_base32_chars)
            translated_base = encoded_base.translate(translation_table)
            decoded = base64.b32decode(translated_base, casefold=True)
            process_decode(decoded.decode('utf-8', 'replace'), 'Base32z')
        except Exception:
            pass

        # 尝试Base36解码
        try:
            if encoded_base.isalnum() and encoded_base.islower():
                decoded = base36.loads(encoded_base)
                process_decode(str(decoded), 'Base36')
        except Exception:
            pass
