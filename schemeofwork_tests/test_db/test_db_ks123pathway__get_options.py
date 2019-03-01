from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import cls_ks123pathway as db_ks123pathway
import db_helper

class test_db_ks123pathway__get_options__year_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_1__topic_1__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands what an algorithm is and is able to express simple linear (non-branching) algorithms symbolically. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Demonstrates care and precision to avoid errors. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_1__topic_2__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 2)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Knows that users can develop their own programs, and can demonstrate this by creating a simple program in an environment that does not rely on text e.g. programmable robots etc. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands that programs execute by following precise instructions. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_1__topic_3__should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 3)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Recognises that digital content can be represented in many forms. (AB) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Distinguishes between some of these forms and can explain the different ways that they communicate information. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_1__topic_4__should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 4)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Understands that computers have no intelligence and that computers can do nothing unless a program is executed. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Recognises that all software executed on digital devices is programmed. (AL) (AB) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_1__topic_5__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 5)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Obtains content from the world wide web using a web browser. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows what to do when concerned about content or being contacted. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_1__topic_6__should_return_5_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 1, topic_id = 6)
        # assert
        self.assertEqual(5, len(rows))
        self.assertEqual("Uses software under the control of the teacher to create, store and edit digital content using appropriate file and folder names. (AB) (GE) (DE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Talks about their work and makes changes to improve it. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_2(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()

    def test__year_2__topic_1__should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 1)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Understands that algorithms are implemented on digital devices as programs. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Detects and corrects errors i.e. debugging, in algorithms. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_2__topic_2__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 2)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Uses arithmetic operators, if statements, and loops, within programs. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Detects and corrects simple semantic errors i.e. debugging, in programs. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_2__topic_3__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 3)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Recognises different types of data: text, number. (AB) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Recognises that data can be structured in tables to make it useful. (AB) (DE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_2__topic_4__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 4)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Recognises that a range of digital devices can be considered a computer. (AB) (GE) ", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands how programs specify the function of a general purpose computer. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_2__topic_5__should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 5)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Navigates the web and can carry out simple web searches to collect digital content. (AL) (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Demonstrates use of computers safely and responsibly, knowing a range of ways to report unacceptable content and contact when online.", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_2__topic_6__should_return_5_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 2, topic_id = 6)
        # assert
        self.assertEqual(5, len(rows))
        self.assertEqual("Uses technology with increasing independence to purposefully organise digital content. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Talks about their work and makes improvements to solutions based on feedback received.(EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_3(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_3__topic_1__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Designs solutions (algorithms) that use repetition and two-way selection i.e. if, then and else. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Uses logical reasoning to predict outputs, showing an awareness of inputs. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_3__topic_2__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 2)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Creates programs that implement algorithms to achieve given goals. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Uses post-tested loop e.g. until, and a sequence of selection statements in programs, including an if, then and else statement. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_3__topic_3__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 3)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands the difference between data and information. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Uses filters or can perform single criteria searches for information.(AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_3__topic_4__should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 4)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Knows that computers collect data from various input devices, including sensors and application software. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the difference between hardware and application software, and their roles within a computer system. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_3__topic_5__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 5)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands the difference between the internet and internet service e.g. world wide web. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Recognises what is acceptable and unacceptable behaviour when using technologies and online services.", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_3__topic_6__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 3, topic_id = 6)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Collects, organises and presents data and information in digital content. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Makes appropriate improvements to solutions based on feedback received, and can comment on the success of the solution. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_4(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_4__topic_1__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Shows an awareness of tasks best completed by humans or computers. (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Recognises that different solutions exist for the same problem. (AL) (AB)", rows[len(rows)-1].objective, "Last item not as expected")



    def test__year_4__topic_2__should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 2)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Understands the difference between, and appropriately uses if and if, then and else statements. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows that a procedure can be used to hide the detail with sub-solution. (AL) (DE) (AB) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_4__topic_3__should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 3)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Performs more complex searches for information e.g. using Boolean and relational operators. (AL) (GE) (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Analyses and evaluates data and information, and recognises that poor quality data leads to unreliable results, and inaccurate conclusions. (AL) (EV)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_4__topic_4__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 4)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands why and when computers are used. (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows the difference between physical, wireless and mobile networks. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_4__topic_5__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 5)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands how to effectively use search engines, and knows how search results are selected, including that search engines use web crawler programs. (AB) (GE) (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Demonstrates responsible use of technologies and online services, and knows a range of ways to report concerns.", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_4__topic_6__should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 4, topic_id = 6)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Makes judgements about digital content when evaluating and repurposing it for a given audience. (EV) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Uses criteria to evaluate the quality of solutions, can identify improvements making some refinements to the solution, and future solutions. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_5(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_5__topic_1__should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 1)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Understands that iteration is the repetition of a process such as a loop. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Can identify similarities and differences in situations and can use these to solve problems (pattern recognition). (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_5__topic_2__should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 2)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Understands that programming bridges the gap between algorithmic solutions and computers. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Selects the appropriate data types. (AL) (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_5__topic_3__should_return_6_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 3)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual("Knows that digital computers use binary to represent all data. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Queries data on one table using a typical query language. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_5__topic_4__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 4)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Recognises and understands the function of the main internal parts of basic computer architecture. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows that there is a range of operating systems and application software for the same hardware. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_5__topic_5__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 5)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands how search engines rank search results. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands data transmission between digital computers over networks, including the internet i.e. IP addresses and packet switching. (AL) (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_5__topic_6__should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 5, topic_id = 6)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Evaluates the appropriateness of digital devices, internet services and application software to achieve given goals. (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Designs criteria to critically evaluate the quality of solutions, uses the criteria to identify improvements and can make appropriate refinements to the solution. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_6(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_6__topic_1_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands a recursive solution to a problem repeatedly applies the same solution to smaller instances of the problem. (AL) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the notion of performance for algorithms and appreciates that some algorithms have different performance characteristics for the same task. (AL) (EV)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_6__topic_2_should_return_6_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 2)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual("Uses nested selection statements. (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Detects and corrects syntactical errors. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_6__topic_3_should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 3)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Understands how numbers, images, sounds and character sets use the same bit patterns. (AB) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Distinguishes between data used in a simple program (a variable) and the storage structure for that data. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_6__topic_4_should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 4)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Understands the von Neumann architecture in relation to the fetchexecute cycle, including how data is stored in memory. (AB) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the basic function and operation of location addressable memory.(AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_6__topic_5_should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 5)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Knows the names of hardware e.g. hubs, routers, switches, and the names of protocols e.g. SMTP, iMAP, POP, FTP, TCP/ IP, associated with networking computer systems. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Uses technologies and online services securely, and knows how to identify and report inappropriate conduct. (AL)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_6__topic_6_should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 6)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Justifies the choice of and independently combines and uses multiple digital devices, internet services and application software to achieve given goals. (EV", rows[0].objective, "First item not as expected")
        self.assertEqual("Designs criteria for users to evaluate the quality of solutions, uses the feedback from the users to identify improvements and can make appropriate refinements to the solution. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_7(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_7__topic_1_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 6, topic_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Understands a recursive solution to a problem repeatedly applies the same solution to smaller instances of the problem. (AL) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the notion of performance for algorithms and appreciates that some algorithms have different performance characteristics for the same task. (AL) (EV)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_7__topic_2_should_return_4_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 7, topic_id = 2)
        # assert
        self.assertEqual(4, len(rows))
        self.assertEqual("Appreciates the effect of the scope of a variable e.g. a local variable cannot be accessed from outside its function. (AB) (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Applies a modular approach to error detection and correction. (AB) (DE) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_7__topic_3_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 7, topic_id = 3)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Knows the relationship between data representation and data quality. (AB)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands how and why values are data typed in many different languages when manipulated within programs. (AB)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_7__topic_4_should_return_1_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 7, topic_id = 4)
        # assert
        self.assertEqual(1, len(rows))
        self.assertEqual("Knows that processors have instruction sets and that these relate to low-level instructions carried out by a computer. (AB) (AL) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows that processors have instruction sets and that these relate to low-level instructions carried out by a computer. (AB) (AL) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_7__topic_5_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 7, topic_id = 5)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Knows the purpose of the hardware and protocols associated with networking computer systems. (AB) (AL)", rows[0].objective, "First item not as expected")
        self.assertEqual("Recognises that persistence of data on the internet requires careful protection of online identity and privacy.", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_7__topic_6_should_return_5_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 7, topic_id = 6)
        # assert
        self.assertEqual(5, len(rows))
        self.assertEqual("Undertakes creative projects that collect, analyse, and evaluate data to meet the needs of a known user group. (AL) (DE) (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Explains and justifies how the use of technology impacts on society, from the perspective of social, economical, political, legal, ethical and moral issues. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_8(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_8__topic_1_should_return_2_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 1)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Designs a solution to a problem that depends on solutions to smaller instances of the same problem (recursion). (AL) (DE) (AB) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands that some problems cannot be solved computationally. (AB) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_8__topic_2_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 2)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Designs and writes nested modular programs that enforce reusability utilising sub-routines wherever possible. (AL) (AB) (GE) (DE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands and uses two dimensional data structures. (AB) (DE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_8__topic_3_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 3)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Performs operations using bit patterns e.g. conversion between binary and hexadecimal, binary subtraction etc. (AB) (AL) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Knows what a relational database is, and understands the benefits of storing data in multiple tables. (AB) (GE) (DE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_8__topic_4_should_return_3_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 4)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Has practical experience of a small (hypothetical) low level programming language. (AB) (AL) (DE) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands and can explain multitasking by computers. (AB) (AL) (DE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_8__topic_5_should_return_1_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 5)
        # assert
        self.assertEqual(1, len(rows))
        self.assertEqual("Understands the hardware associated with networking computer systems, including WANs and LANs, understands their purpose and how they work, including MAC addresses. (AB) (AL) (DE) (GE)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the hardware associated with networking computer systems, including WANs and LANs, understands their purpose and how they work, including MAC addresses. (AB) (AL) (DE) (GE)", rows[len(rows)-1].objective, "Last item not as expected")


    def test__year_8__topic_6_should_return_1_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 8, topic_id = 6)
        # assert
        self.assertEqual(1, len(rows))
        self.assertEqual("Understands the ethical issues surrounding the application of information technology, and the existence of legal frameworks governing its use e.g. Data Protection Act, Computer Misuse Act, Copyright etc. (EV)", rows[0].objective, "First item not as expected")
        self.assertEqual("Understands the ethical issues surrounding the application of information technology, and the existence of legal frameworks governing its use e.g. Data Protection Act, Computer Misuse Act, Copyright etc. (EV)", rows[len(rows)-1].objective, "Last item not as expected")


class test_db_ks123pathway__get_options__year_9(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_9__topic_1_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_9__topic_2_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_9__topic_3_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 3)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_9__topic_4_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 4)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_9__topic_5_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 5)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_9__topic_6_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 9, topic_id = 6)
        # assert
        self.assertEqual(0, len(rows))


class test_db_ks123pathway__get_options__year_10(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_10__topic_1_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 1)
        # assert
        self.assertEqual(0, len(rows))

    def test__year_10__topic_2_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_10__topic_3_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 3)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_10__topic_4_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 4)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_10__topic_5_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 5)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_10__topic_6_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 10, topic_id = 6)
        # assert
        self.assertEqual(0, len(rows))


class test_db_ks123pathway__get_options__year_11(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_11__topic_1_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_11__topic_2_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_11__topic_3_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 3)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_11__topic_4_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 4)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_11__topic_5_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 5)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_11__topic_6_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 11, topic_id = 6)
        # assert
        self.assertEqual(0, len(rows))


class test_db_ks123pathway__get_options__year_12(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_12__topic_1_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_12__topic_2_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_12__topic_3_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 3)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_12__topic_4_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 4)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_12__topic_5_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 5)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_12__topic_6_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 12, topic_id = 6)
        # assert
        self.assertEqual(0, len(rows))


class test_db_ks123pathway__get_options__year_13(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__year_13__topic_1_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_13__topic_2_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_13__topic_3_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 3)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_13__topic_4_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 4)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_13__topic_5_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 5)
        # assert
        self.assertEqual(0, len(rows))


    def test__year_13__topic_6_should_return_x_items(self):
        # test
        rows = db_ks123pathway.get_options(self.fake_db, year_id = 13, topic_id = 6)
        # assert
        self.assertEqual(0, len(rows))

