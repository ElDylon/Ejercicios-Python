texto = ''' NumPy is the fundamental package needed for scientific computing with Python.

    Website: https://www.numpy.org
    Documentation: https://numpy.org/doc
    Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
    Source code: https://github.com/numpy/numpy
    Contributing: https://www.numpy.org/devdocs/dev/index.html
    Bug reports: https://github.com/numpy/numpy/issues
    Report a security vulnerability: https://tidelift.com/docs/security

It provides:

    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities

Testing:

    NumPy versions ≥ 1.15 require pytest
    NumPy versions < 1.15 require nose

Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'

Call for Contributions

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

    review pull requests
    triage issues
    develop tutorials, presentations, and other educational materials
    maintain and improve our website
    develop graphic design for our brand assets and promotional materials
    translate website content
    help with outreach and onboard new contributors
    write grant proposals and help with other fundraising efforts

If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invite).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.

Powered by NumFOCUS
About

The fundamental package for scientific computing with Python.
numpy.org
Topics
python numpy
Resources
Readme
License
BSD-3-Clause License
Releases 183
v1.20.1 Latest
on 7 Feb
+ 182 releases
Sponsor this project

    @numfocus
    numfocus NumFOCUS

    tidelift tidelift.com/funding/github/pypi/numpy

    https://numpy.org/about/

Learn more about GitHub Sponsors
Packages
No packages published
Used by 617k

    @sktatsuno
    @Andy-CH-BO-AN
    @sinablk
    @bartmch
    @dydwkd486
    @mochibbb
    @ishujais
    @khoa-luan

+ 617,044
Contributors 1,083

    @charris
    @teoliphant
    @mattip
    @cournape
    @eric-wieser
    @seberg
    @pearu
    @rgommers
    @pv
    @juliantaylor
    @mwiebe

+ 1,072 contributors
Languages

Python 63.4%
C 35.3%
C++ 1.0%
JavaScript 0.1%
Fortran 0.1%
Shell 0.1%'''

def palabra_maximo(texto):
    palabras_texto = texto.split(" " or '')
    for i in palabras_texto:
        i.strip().lower()
    palabras_texto.sort()
    frecuencia_palabras = [palabras_texto.count(p) for p in palabras_texto]
    conteo_palabras = list(zip(palabras_texto, frecuencia_palabras))
    print(palabras_texto)
    print(frecuencia_palabras)
    print(conteo_palabras)

palabra_maximo(texto)
