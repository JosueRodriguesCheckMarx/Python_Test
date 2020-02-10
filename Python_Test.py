import asyncio
import datetime
import os
import math
import pathlib
import statistics

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

def fn(a, b, c, d):
    print(a, b, c, d)

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

class Test:
    def start():
        # 3.5
        Test.PEP_465()
        Test.PEP_448()
        asyncio.run(Test.PEP_492())
        Test.PEP_461()
        # 3.6
        Test.PEP_498()
        Test.PEP_526()
        Test.PEP_515()
        asyncio.run(Test.PEP_530())
        #3.7
        Test.PEP_563()
        # 3.8
        Test.PEP_572()
        Test.PEP_570()
        Test.PEP_498_2()

        # Features

        # 3.5
        Test.PEP_485()
        # 3.6
        Test.PEP_519()
        # 3.7
        Test.PEP_539()
        #Test.PEP_564()
        # 3.8
        Test._math38_()
        Test._adddlldirectory_()
        Test._path_()
        Test._statistics_()
        Test._xml_()

    # =============================================================================
    #
    # Syntax
    #
    # =============================================================================

    async def PEP_492():
            import time
            print("PEP 492")
            print(f"started at {time.strftime('%X')}")
            await asyncio.sleep(1)
            print('Hello')
            await asyncio.sleep(1)
            print('World')
            print(f"finished at {time.strftime('%X')}")
            print("--------")

    def PEP_465():
        print("PEP 465")
        # S = (H @ beta - r).T @ inv(H @ V @ H.T) @ (H @ beta - r)
        print("N/A ")
        print("--------")

    def PEP_448():
        print("PEP 448")
        print(*[1], *[2], 3, *[4, 5])
        fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
        print("--------")

    def PEP_461():
        print("PEP 461")
        print(b'Hello %b!' % b'World')
        print(b'x=%i y=%f' % (1, 2.5))
        print("--------")

    def PEP_498():
        print("PEP 498")
        name = "Fred"
        print(f"He said his name is {name}.")
        #  the correct way to have a literal brace appear in the resulting string value is to double the brace:
        print(f'{{{4*10}}}')
        print("--------")

    def PEP_526():
        print("PEP 526")
        value=1
        var = value  # type: annotation
        var: annotation; var = value
        var: annotation = value
        print('Annotation Test')
        print("--------")

    def PEP_515():
        print("PEP 515")
        print(1_000_000_000_000_000)
        print(0x_FF_FF_FF_FF)
        print('{:_}'.format(1000000))
        print('{:_x}'.format(0xFFFFFFFF))
        print("--------")

    async def PEP_530():
        print("PEP 530")
        print("N/A ")
        print("--------")

    def PEP_563():
        print("PEP 563")
        print("N/A ")
        print("--------")

    def PEP_572():
        print("PEP 572")
        a = '12345678901234567890'
        if (n := len(a)) > 10:
            print(f"List is too long ({n} elements, expected <= 10)")

        print("--------")

    def PEP_570():
        print("PEP 570")
        f(10, 20, 30, d=40, e=50, f=60)
        print("--------")

    def PEP_498_2():
        print("PEP 498_Change")
        user = 'eric_idle'
        member_since = datetime.datetime(1975, 7, 31)
        print(f'{user=} {member_since=}')
        print("--------")


# =============================================================================
#
# Features
#
# =============================================================================

    def PEP_485():
        print("PEP 485")
        a = 5.0
        b = 4.99998
        print(math.isclose(a, b, rel_tol=1e-5))     #True
        print(math.isclose(a, b, rel_tol=1e-6))     #False
        print(math.isclose(a, b, abs_tol=0.00003))  #True
        print(math.isclose(a, b, abs_tol=0.00001))  #False
        print("--------")

    def PEP_519():
        print("PEP 519")
        with open(pathlib.Path("Python_Test.py")) as f:
            contents = f.read()
        print(os.path.splitext(pathlib.Path("some_file.txt")))
        print(os.path.join("/a/b", pathlib.Path("c")))
        print(os.fspath(pathlib.Path("some_file.txt")))
        print("--------")

    def PEP_539():
        print("PEP 539")



        print("--------")

    def PEP_564():
        import time

        print("PEP 564")
        print(time.time())
        timee = time.time()
        timeee=time.clock_gettime_ns()
        print(timeee)
        print(time.clock_settime_ns(time.time(), 10000000))
        print('---')
        print(time.time())
        time.clock_settime_ns(timee, 0)
        print(time.time())
        print('-----')
        print(time.monotonic_ns())
        print(time.perf_counter_ns())
        print(time.process_time_ns())
        print(time.time_ns())
        print("--------")

    def _math38_():

        prior = 0.8
        likelihoods = [0.625, 0.84, 0.30]
        r = 650320427
        s = r ** 2
        print("3.8 math")
        print(math.dist([3],[-8]))
        print(math.hypot(1,1))
        print(math.prod(likelihoods, start=prior))
        print(math.perm(10, 3))
        print(math.comb(10, 3))
        print(math.isqrt(s - 1))
        print("--------")


    def _adddlldirectory_():

        print("add_dll_directory")
        path = 'c:/'
        os.add_dll_directory(path)
        print("--------")

    def _path_():
        print("os.path")

        path = "c:/"

        print(os.path.abspath(path))
        print(os.path.basename(path))
        print(os.path.commonpath(['/windows', '/windows/system32']))
        print(os.path.commonprefix(['/windows', '/windows/system32']))

        print(os.path.exists(path))     #True
        print(os.path.lexists(path))    #True
        print(os.path.isdir(path))      #True
        print(os.path.isfile(path))     #False
        print(os.path.islink(path))     #False
        print(os.path.ismount(path))    #True

        print("--------")

    def _statistics_():
        print("Statistics")
        print("--")
        print(statistics.fmean([3.5, 4.0, 5.25]))
        print("--")
        print(round(statistics.geometric_mean([54, 24, 36]), 1))
        print("--")
        temperature_feb = statistics.NormalDist.from_samples([4, 12, -3, 2, 7, 14])
        print(temperature_feb.mean)
        print(temperature_feb.stdev)
        print(temperature_feb.cdf(3))
        print(temperature_feb.pdf(7) / temperature_feb.pdf(10))
        el_niño = statistics.NormalDist(4, 2.5)
        temperature_feb += el_niño
        print(temperature_feb)
        statistics.NormalDist(mu=10.0, sigma=6.830080526611674)
        temperature_feb * (9 / 5) + 32
        statistics.NormalDist(mu=50.0, sigma=12.294144947901014)
        print(temperature_feb.samples(3))
        print("--------")

    def _xml_():
        from xml.dom.minidom import parse, parseString
        dom1 = parse('C:\Windows\\PrintDialog\\appxmanifest.xml')
        datasource = open('C:\Windows\\PrintDialog\\appxmanifest.xml')
        dom2 = parse(datasource)
        dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')
        print(dom2)
        print(dom3)


# =============================================================================
# Author : Josué Rodrigues
# Description: Test features
# Date : 02-2020
# =============================================================================


Test.start()