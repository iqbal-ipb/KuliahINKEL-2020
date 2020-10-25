
from koboextractor import KoboExtractor
kobo = KoboExtractor('Token 3a3a029eda62dda42873aa49033de9b108475df4',
                     'https://kf2.pemantau.id/api/v2')
asset = kobo.get_asset('afW8mQQsZyUeCfyRaDMU8J')
