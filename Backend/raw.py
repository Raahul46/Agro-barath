from yandex.Translater import Translater
tr = Translater()
tr.set_key('trnsl.1.1.20200119T075806Z.ba2fc76141b64141.3739322923782504e521bd76c8903e90835cb864')
tr.set_from_lang('en')
tr.set_to_lang('ta')
tr.set_text("rice crop field few weeks after sowing of seeds.")
txt = tr.translate()
