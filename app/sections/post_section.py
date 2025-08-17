from bs4 import BeautifulSoup
from app.locators.section_locators import SectionLocator
from app.parsers.post import PostParser

'''
<html
  lang="en"
  class="sizes customelements history pointerevents postmessage webgl websockets cssanimations csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox picture srcset webworkers"
>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>UniBEN - HOME</title>

    <!--====== Favicon Icon ======-->
    <link rel="shortcut icon" href="images/uniben_logo.jpg" type="image/jpg" />

    <!--====== Slick css ======-->
    <link rel="stylesheet" href="css/slick.css" />

    <!--====== Animate css ======-->
    <link rel="stylesheet" href="css/animate.css" />

    <!--====== Nice Select css ======-->
    <link rel="stylesheet" href="css/nice-select.css" />

    <!--====== Nice Number css ======-->
    <link rel="stylesheet" href="css/jquery.nice-number.min.css" />

    <!--====== Magnific Popup css ======-->
    <link rel="stylesheet" href="css/magnific-popup.css" />

    <!--====== Bootstrap css ======-->
    <link rel="stylesheet" href="css/bootstrap.min.css" />

    <!--====== Fontawesome css ======-->
    <link rel="stylesheet" href="css/font-awesome.min.css" />

    <!--====== Default css ======-->
    <link rel="stylesheet" href="css/default.css" />

    <!--====== Style css ======-->
    <link rel="stylesheet" href="css/style.css" />

    <!--====== My Style css ======-->
    <link rel="stylesheet" href="css/mystyle.css" />

    <!--====== Responsive css ======-->
    <link rel="stylesheet" href="css/responsive.css" />

    <style>
      .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 5px;
        align-items: start;
        justify-items: center;
      }

      .grid img {
        border: 1px solid rgba(0, 0, 0, 0.3);
        box-shadow: 2px 2px 6px 0px rgba(0, 0, 0, 0.3);
        max-width: 100%;
      }

      .grid img:nth-child(2) {
        grid-column: span 3;
        grid-row: span 2;
      }

      .grid img:nth-child(4) {
        grid-column: span 2;
        grid-row: span 2;
      }

      /* .grid img:nth-child(1) {
            grid-column: span 2;
            grid-row: span 1;
            }
            .grid img:nth-child(2) {
            grid-column: span 1;
            grid-row: span 2;
            }
            .grid img:nth-child(3) {
            grid-column: span 1;
            grid-row: span 2;
            }
            .grid img:nth-child(4) {
            grid-column: span 1;
            grid-row: span 2;
            }
            .grid img:nth-child(5) {
            grid-column: span 1;
            grid-row: span 2;
            }
            .grid img:nth-child(8) {
            grid-column: span 2;
            grid-row: span 1;
            } */
      .slider-container {
        position: relative;
        width: 100%;
        overflow: hidden;
        text-align: center;
      }

      .slider {
        display: flex;
        transition: transform 0.5s linear;
      }

      .slide {
        width: 40%;
        /* Adjust based on the number of images */
        flex-shrink: 0;
        text-align: center;
        position: relative;
      }

      .slide img {
        width: 100%;
        height: auto;
      }

      .caption {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.5);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
      }
    </style>
  </head>

  <body>
    <!--====== PRELOADER PART START ======-->

    <div class="preloader" style="display: none">
      <div class="loader rubix-cube">
        <div class="layer layer-1"></div>
        <div class="layer layer-2"></div>
        <div class="layer layer-3 color-1"></div>
        <div class="layer layer-4"></div>
        <div class="layer layer-5"></div>
        <div class="layer layer-6"></div>
        <div class="layer layer-7"></div>
        <div class="layer layer-8"></div>
      </div>
    </div>

    <!--====== PRELOADER PART START ======-->

    <!--====== HEADER PART START ======-->

    <header id="header-part">
      <div class="header-top d-block">
        <div class="container">
          <div class="row">
            <div class="col-lg-6">
              <div class="header-contact text-lg-left text-center">
                <img src="images/logo-1.png" alt="UNIBEN Logo" />
              </div>
            </div>
            <div class="col-lg-6">
              <div class="header-opening-time text-lg-right text-center">
                <div class="serach-form">
                  <form action="#">
                    <input
                      class="search-input"
                      type="text"
                      placeholder="Search by keyword"
                    />
                    <button class="search-button">
                      <i class="fa fa-search"></i>
                    </button>
                  </form>
                  <img src="images/all-icon/email.png" alt="icon" /><span
                    style="color: white"
                    >registrar@uniben.edu</span
                  >
                  &nbsp; <img src="images/all-icon/email.png" alt="icon" /><span
                    style="color: white"
                    >senatematters@uniben.edu</span
                  >
                </div>
              </div>
            </div>
          </div>
          <!-- row -->
        </div>
        <!-- container -->
      </div>
      <!-- header top -->

      <div class="navigation">
        <div class="container">
          <div class="row">
            <div class="col-lg-10 col-md-10 col-sm-9 col-8">
              <nav class="navbar navbar-expand-lg">
                <button
                  class="navbar-toggler"
                  type="button"
                  data-toggle="collapse"
                  data-target="#navbarSupportedContent"
                  aria-controls="navbarSupportedContent"
                  aria-expanded="false"
                  aria-label="Toggle navigation"
                >
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>

                <div
                  class="collapse navbar-collapse sub-menu-bar"
                  id="navbarSupportedContent"
                >
                  <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                      <a href="index.html" class="primary-menu-item">Home</a>
                    </li>
                    <li class="nav-item">
                      <a href="#" class="primary-menu-item"
                        >About<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li><a href="about.html">About UNIBEN</a></li>
                        <li><a href="about-uniben.html">History</a></li>
                        <li>
                          <a href="vchancellor.html"
                            >Vice-Chancellor's Office</a
                          >
                        </li>
                        <li>
                          <a href="offices-units.html">Offices and Units</a>
                        </li>
                        <li>
                          <a href="principal-staff.html">Principal Staff</a>
                        </li>
                        <li>
                          <a href="council-members.html">Members of Council</a>
                        </li>
                        <!--<li><a href="servicom-charter.html">Servicom Charter</a></li>-->
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a
                        href="https://unibenportal.com/"
                        class="primary-menu-item"
                        >Admissions<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li>
                          <a href="why_choose_uniben.html">Why Choose UNIBEN</a>
                        </li>
                        <li>
                          <a href="admission_policy.html">Admission Policy</a>
                        </li>
                        <li>
                          <a href="https://unibenportal.com" target="_blank"
                            >Apply to UNIBEN</a
                          >
                        </li>
                        <li>
                          <a href="https://unibenportal.com" target="_blank"
                            >Undergraduate Application</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://waeup.uniben.edu/applicants/pg2023"
                            target="_blank"
                            >Post-Graduate Application</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://waeup.uniben.edu/applicants/pre2024"
                            target="_blank"
                            >Foundation Programmes (JUPEB)</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="#" class="primary-menu-item"
                        >Academics<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li>
                          <a href="schoolsandfaculties.html"
                            >Schools and Faculties</a
                          >
                        </li>
                        <li>
                          <a href="institutes.html">Institutes and Centres</a>
                        </li>
                        <li>
                          <a
                            href="https://academicplanning.uniben.edu/"
                            target="_blank"
                            >Academic Planning</a
                          >
                        </li>
                        <li>
                          <a href="https://cdl.uniben.edu/" target="_blank"
                            >Centre for Distance Learning</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://alumni.uniben.edu/applicants/checktranscript/"
                            target="_blank"
                            >Transcript</a
                          >
                        </li>
                        <li>
                          <a href="https://qa.uniben.edu/" target="_blank"
                            >Quality Assurance</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="#" class="primary-menu-item"
                        >Resources<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li>
                          <a
                            href="https://usimp.uniben.edu/login.html"
                            target="_blank"
                            >Abstracts</a
                          >
                        </li>
                        <li>
                          <a href="https://journaldb.uniben.edu/">Journals</a>
                        </li>
                        <li>
                          <a
                            href="https://ir.uniben.edu/newgenlibctxt/"
                            target="_blank"
                            >Institutional Repository</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://uniben.edu/staff_profiles.html"
                            target="_blank"
                            >Staff Profiles</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://usimp.uniben.edu/login.html"
                            target="_blank"
                            >Registry Staff Update</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://news.uniben.edu/category/inaugurals/"
                            target="_blank"
                            >Inaugural Lectures</a
                          >
                        </li>
                        <li>
                          <a href="https://jhl.uniben.edu/" target="_blank"
                            >Library Facility</a
                          >
                        </li>
                        <li>
                          <a href="https://mail.google.com/" target="_blank"
                            >Staff Email</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="blog.html" class="primary-menu-item"
                        >StudentLife<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li><a href="campus-life.html">Campus Life</a></li>
                        <li>
                          <a href="https://uniben.edu/hostels.html">Hostels</a>
                        </li>
                        <li>
                          <a href="entrepreneurship.html">Entrepreneurship</a>
                        </li>
                        <li>
                          <a href="https://uniben.edu/work-study.html"
                            >Work and Study</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://docs.google.com/forms/d/e/1FAIpQLSdYNXWck3fqrnKs_6q8qfPmShycoIHRLuUH-wZdi0iV6aoerw/viewform"
                            >Internet Request</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://studentaffairs.uniben.edu/"
                            target="_blank"
                            >Student Affairs</a
                          >
                        </li>
                        <li><a href="#">Exams and Records</a></li>

                        <li>
                          <a
                            href="https://uniben.edu/guidanceandcounselling.html"
                            >Guidance and Counselling</a
                          >
                        </li>
                        <li>
                          <a href="https://uniben.edu/health-centre.html"
                            >Health Service</a
                          >
                        </li>
                        <li><a href="#">Sexual Abuse Policy</a></li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="#" class="primary-menu-item"
                        >Updates<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li><a href="https://news.uniben.edu/">News</a></li>
                        <li>
                          <a href="https://news.uniben.edu/category/events/"
                            >Events</a
                          >
                        </li>
                        <li>
                          <a href="https://news.uniben.edu/?s=Research"
                            >Research News</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://tetfunddesk.uniben.edu/"
                            target="_blank"
                            >TetFund</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="#" class="primary-menu-item"
                        >Information<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li><a href="alumni.html">Alumni</a></li>

                        <li>
                          <a href="https://qa.uniben.edu/?p=127">Policies</a>
                        </li>

                        <li><a href="partners.html">Our Partners</a></li>
                        <li>
                          <a href="https://uniben.edu/servicom-charter.html"
                            >Servicom</a
                          >
                        </li>
                        <li>
                          <a href="https://iptto.uniben.edu/" target="_blank"
                            >Intellectual Property</a
                          >
                        </li>
                        <li>
                          <a
                            href="https://news.uniben.edu/vital-financial-data/"
                            target="_blank"
                            >Key Insitutional Information</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li class="nav-item">
                      <a href="contact.html" class="primary-menu-item"
                        >Contact<button class="sub-nav-toggler">
                          <i class="fa fa-chevron-down"></i></button
                      ></a>
                      <ul class="sub-menu">
                        <li><a href="contact.html">Contact Us</a></li>

                        <li>
                          <a href="https://uniben.edu/pro-office.html"
                            >PRO Office</a
                          >
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </nav>
              <!-- nav -->
            </div>
            <!-- <div class="col-lg-2 col-md-2 col-sm-3 col-4">
                        <div class="right-icon text-right">
                            <ul>
                                <li><a href="#" id="search"><i class="fa fa-search"></i></a></li>
                                <li><a href="#"><i class="fa fa-shopping-bag"></i><span>0</span></a></li>
                            </ul>
                        </div> <!-- right icon 
                    </div> -->
          </div>
          <!-- row -->
        </div>
        <!-- container -->
      </div>
    </header>

    <!--====== HEADER PART ENDS ======-->

    <!--====== SEARCH BOX PART START ======-->

    <div class="search-box">
      <div class="serach-form">
        <div class="closebtn">
          <span></span>
          <span></span>
        </div>
        <form action="#">
          <input type="text" placeholder="Search by keyword" />
          <button><i class="fa fa-search"></i></button>
        </form>
      </div>
      <!-- serach form -->
    </div>

    <!--====== SEARCH BOX PART ENDS ======-->

    <!--====== SLIDER PART START ======-->

    <section
      id="slider-part"
      class="slider-active slick-initialized slick-slider"
    >
      <span class="prev slick-arrow" style="display: block"
        ><i class="fa fa-angle-left"></i
      ></span>

      <!--<div class="single-slider bg_cover pt-150" style="background-image: url(images/slider/eng_students.JPG)" data-overlay="4">
            <div class="container">
                <div class="row">
                    <div class="col-xl-7 col-lg-9">
                        <div class="slider-cont">
                            <h1 data-animation="bounceInLeft" data-delay="1s">Engineering Laboratory Workshop</h1>
                            <p data-animation="fadeInUp" data-delay="1.3s">Students take part in Laboratory Workshop Practicals in the Faculty of Engineering.</p>
                            <ul>
                                <li><a data-animation="fadeInUp" data-delay="1.6s" class="main-btn" href="https://eng.uniben.edu">Visit Engineering</a></li>
                                <!-- <li><a data-animation="fadeInUp" data-delay="1.9s" class="main-btn main-btn-2" href="#">Get Started</a></li> 
                            </ul>
                        </div>
                    </div>
                </div> 
            </div> 
</div>  single slider -->
      <!-- Admission single slider -->
      <div class="slick-list draggable">
        <div class="slick-track" style="opacity: 1; width: 6340px">
          <div
            class="single-slider bg_cover pt-150 slick-slide slick-current slick-active"
            style="
              background-image: url('images/slider/admission.jpg');
              width: 1585px;
              position: relative;
              left: 0px;
              top: 0px;
              z-index: 999;
              opacity: 1;
            "
            data-overlay="4"
            data-slick-index="0"
            aria-hidden="false"
            tabindex="0"
          >
            <div class="container">
              <div class="row">
                <div class="col-xl-7 col-lg-9">
                  <div class="slider-cont">
                    <h1
                      data-animation="bounceInLeft"
                      data-delay="1s"
                      class=""
                      style="animation-delay: 1s"
                    >
                      2025 / 2026 Post-UTME Screening
                    </h1>
                    <p
                      data-animation="fadeInUp"
                      data-delay="1.3s"
                      class=""
                      style="animation-delay: 1.3s"
                    >
                      The University of Benin (UNIBEN) has announced the
                      commencement of its Admission Screening Exercise for the
                      2025/2026 academic session. The application process is
                      scheduled to begin on Monday, 4th August 2025, at 8:00 AM
                      and closes on Friday, 22nd August
                      2025&nbsp;at&nbsp;Midnight.
                    </p>
                    <ul>
                      <li>
                        <a
                          data-animation="fadeInUp"
                          data-delay="1.6s"
                          class="main-btn"
                          href="https://unibenportal.com/"
                          target="_blank"
                          tabindex="0"
                          style="animation-delay: 1.6s"
                          >Click to Apply</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
          <div
            class="single-slider bg_cover pt-150 slick-slide"
            style="
              background-image: url('images/slider/uniben_entrance.JPG');
              width: 1585px;
              position: relative;
              left: -1585px;
              top: 0px;
              z-index: 998;
              opacity: 0;
              transition: opacity 500ms;
            "
            data-overlay="4"
            data-slick-index="1"
            aria-hidden="true"
            tabindex="-1"
          >
            <div class="container">
              <div class="row">
                <div class="col-xl-7 col-lg-9">
                  <div class="slider-cont">
                    <h1
                      data-animation="bounceInLeft"
                      data-delay="1s"
                      class=""
                      style="animation-delay: 1s"
                    >
                      Welcome to the University of Benin
                    </h1>
                    <p
                      data-animation="fadeInUp"
                      data-delay="1.3s"
                      class=""
                      style="animation-delay: 1.3s"
                    >
                      One of Nigeria’s most prestigious universities, known for
                      its academic excellence and rich history.
                    </p>
                    <ul>
                      <li>
                        <a
                          data-animation="fadeInUp"
                          data-delay="1.6s"
                          class="main-btn"
                          href="https://uniben.edu/about.html"
                          tabindex="-1"
                          style="animation-delay: 1.6s"
                          >Read More</a
                        >
                      </li>
                      <!-- <li><a data-animation="fadeInUp" data-delay="1.9s" class="main-btn main-btn-2" href="#">Get Started</a></li> -->
                    </ul>
                  </div>
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
          <div
            class="single-slider bg_cover pt-150 slick-slide"
            style="
              background-image: url('images/slider/ROM_4981.JPG');
              width: 1585px;
              position: relative;
              left: -3170px;
              top: 0px;
              z-index: 998;
              opacity: 0;
              transition: opacity 500ms;
            "
            data-overlay="4"
            data-slick-index="2"
            aria-hidden="true"
            tabindex="-1"
          >
            <div class="container">
              <div class="row">
                <div class="col-xl-7 col-lg-9">
                  <div class="slider-cont">
                    <h1
                      data-animation="bounceInLeft"
                      data-delay="1s"
                      class=""
                      style="animation-delay: 1s"
                    >
                      Academics Bring Excellence
                    </h1>
                    <p
                      data-animation="fadeInUp"
                      data-delay="1.3s"
                      class=""
                      style="animation-delay: 1.3s"
                    >
                      Students of the Faculty of Physical Sciences carrying out
                      experimental work in the field.
                    </p>
                    <ul>
                      <li>
                        <a
                          data-animation="fadeInUp"
                          data-delay="1.6s"
                          class="main-btn"
                          href="https://physci.uniben.edu/"
                          target="_blank"
                          tabindex="-1"
                          style="animation-delay: 1.6s"
                          >Visit Physical Sciences</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
          <div
            class="single-slider bg_cover pt-150 slick-slide"
            style="
              background-image: url('images/slider/IMG_0906.JPG');
              width: 1585px;
              position: relative;
              left: -4755px;
              top: 0px;
              z-index: 998;
              opacity: 0;
              transition: opacity 500ms;
            "
            data-overlay="4"
            data-slick-index="3"
            aria-hidden="true"
            tabindex="-1"
          >
            <div class="container">
              <div class="row">
                <div class="col-xl-7 col-lg-9">
                  <div class="slider-cont">
                    <h1
                      data-animation="fadeInLeft"
                      data-delay="1s"
                      class=""
                      style="animation-delay: 1s"
                    >
                      Learning By Practicing
                    </h1>
                    <p
                      data-animation="fadeInUp"
                      data-delay="1.3s"
                      class=""
                      style="animation-delay: 1.3s"
                    >
                      University of Benin endeavours to instill enterpreneurship
                      skills to students. This in turn creates qualified
                      manpower for the industry.
                    </p>
                    <ul>
                      <li>
                        <a
                          data-animation="fadeInUp"
                          data-delay="1.6s"
                          class="main-btn"
                          href="#"
                          tabindex="-1"
                          style="animation-delay: 1.6s"
                          >Read More</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
        </div>
      </div>
      <!-- single slider -->
      <!-- End Admission single slider -->

      <!-- single slider -->

      <!--<div class="single-slider bg_cover pt-150" style="background-image: url(images/slider/matric_banner.jpg)" data-overlay="4">
            <div class="container">
                <div class="row">
                    <div class="col-xl-7 col-lg-9">
                        <div class="slider-cont">
                            <h1 data-animation="bounceInLeft" data-delay="1s">2024/2025 Matriculation</h1>
                            <p data-animation="fadeInUp" data-delay="1.3s">Congratulations to all Admitted Students</p>
                            <ul>
                                <li><a data-animation="fadeInUp" data-delay="1.6s" class="main-btn" href="https://news.uniben.edu/live-event-matriculation-2025/" target="_blank">Watch Live</a>
                                
                            </ul>
                        </div>
                    </div>
                </div> <!-- row 
            </div> <!-- container 
        </div> 

<!-- single slider -->
      <!-- single slider -->
      <!-- single slider -->
      <span class="next slick-arrow" style="display: block"
        ><i class="fa fa-angle-right"></i
      ></span>
    </section>

    <!--====== SLIDER PART ENDS ======-->

    <!--====== EXAMPLE SLIDER PART ========-->

    <section
      id="slider-part1"
      class="slider-active slick-initialized slick-slider"
    >
      <div class="slick-list draggable">
        <div class="slick-track" style="opacity: 1; width: 0px"></div>
      </div>
    </section>

    <!--====== EXAMPLE SLIDER PART END ========-->

    <!--====== EXAMPLE SLIDER PART END ========-->

    <!--====== COURSE PART START ======-->
    <!--====== COURSE PART START ======-->
    <section id="course-part" class="gray-bg">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <div class="section-title pb-45">
              <br />
              <h5>
                <a href="https://news.uniben.edu/" style="color: #9c0c84"
                  >All News</a
                >
              </h5>
              <h2>NEWS</h2>
            </div>
          </div>
        </div>

        <div class="row course-slied mt-30 slick-initialized slick-slider">
          <span class="prev slick-arrow" style="display: block"
            ><i class="fa fa-angle-left"></i
          ></span>

          <!-- NEWS ITEM 1 -->
          <div class="slick-list draggable">
            <div
              class="slick-track"
              style="
                opacity: 1;
                width: 11600px;
                transform: translate3d(-4400px, 0px, 0px);
                transition: transform 800ms;
              "
            >
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="-3"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/elecrtification project.png"
                        alt="Solar Intervention"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Solar Intervention</span>
                    <a
                      href="https://news.uniben.edu/uniben-named-as-beneficiary-of-federal-government-solar-minigrid-intervention/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN NAMED AS BENEFICIARY OF FEDERAL GOVERNMENT SOLAR
                        MINIGRID INTERVENTION
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="-2"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/unibenev.jpg" alt="EV Award" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >UNIBEN Clinches Victory in National Electric Vehicle
                      Design Contest</span
                    >
                    <a
                      href="https://news.uniben.edu/uniben-clinches-victory-in-national-electric-vehicle-design-contest-earns-n5-million-prize/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN Clinches Top Prize at NADDC’s National EV Design
                        Competition!
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="-1"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/tetfundLoan.jpg" alt="tetfund" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >Tertiary Institutions Staff Support Fund (TISSF)</span
                    >
                    <a
                      href="https://news.uniben.edu/tertiary-institutions-staff-support-fund-tissf/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        - A Federal Ministry of Education and Tetfund funded
                        program
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="0"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/vc_welcome.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Vice Chancellor</span>
                    <a href="..." target="_blank" tabindex="-1">
                      <h4>Welcome Address by VC...</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="1"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/admission.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>2025/2026 Admission</span>
                    <a
                      href="https://unibenportal.com/#application"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>APPLY FOR POST-UTME SCREENING</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="2"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/ize-iyamu.jpeg" alt="UBTH CMD" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>PROFESSOR IDIA IZE – IYAMU</span>
                    <a
                      href="https://news.uniben.edu/professor-idia-ize-iyamu-is-new-cmd-of-ubth/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>NEW Chief Medical Director OF UBTH</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="3"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/vc_collaboration.jpeg"
                        alt="Course"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Promoting New Knowledge</span>
                    <a
                      href="https://news.uniben.edu/uniben-vc-canvasses-increased-afro-centric-collaborations-to-promote-new-knowledge/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN VC CANVASSES INCREASED AFRO–CENTRIC
                        COLLABORATIONS
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="4"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/unibenvc.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Sports Development</span>
                    <a
                      href="https://news.uniben.edu/uniben-vc-appointed-to-serve-on-high-powered-ministerial-committee-on-review-of-sports-courses-and-curricula-in-tertiary-institutions-as-uniben-is-selected-as-sports-centre-of-excellence/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN VC APPOINTED TO SERVE ON HIGH POWERED MINISTERIAL
                        COMMITTEE
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="5"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/FG_COMPLIANCE.jpeg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FEDERAL GOVERNMENT TEAM</span>
                    <a
                      href="https://news.uniben.edu/federal-government-team-at-uniben-to-ascertain-compliance-with-presidential-white-paper-on-visitation-panel-report/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        TO ASCERTAIN COMPLIANCE WITH PRESIDENTIAL WHITE PAPER ON
                        VISITATION PANEL REPORT
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="6"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/21669.jpg" alt="exchange" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>TEACHER- STUDENT EXCHANGE PROGRAMME</span>
                    <a
                      href="https://news.uniben.edu/collaborative-meeting-between-university-of-benin-and-fujian-jiangxia-university-held-at-ugbowo-campus-university-of-benin-benin-city/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN SIGNS MOU WITH FUJIAN JIANGXIA UNIVERSITY, CHINA,
                        ON TEACHER- STUDENT EXCHANGE PROGRAMME
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="7"
                aria-hidden="true"
                tabindex="0"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/forensic.jpg" alt="forensic" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FORENSIC AND DNA TRAINING</span>
                    <a
                      href="https://news.uniben.edu/uniben-begins-talks-with-the-police-service-commission-on-imperative-of-forensic-and-dna-training-for-psc-personnel-and-the-police/"
                      target="_blank"
                      tabindex="0"
                    >
                      <h4>
                        UNIBEN BEGINS TALKS WITH THE POLICE SERVICE COMMISSION
                        ON IMPERATIVE OF FORENSIC AND DNA TRAINING FOR PSC
                        PERSONNEL AND THE POLICE
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-current slick-active"
                data-slick-index="8"
                aria-hidden="false"
                tabindex="0"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/emr1.PNG" alt="World Bank" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>World Bank ACE Audit</span>
                    <a
                      href="https://news.uniben.edu/esmp-audit-of-the-ace-impact-project/"
                      target="_blank"
                      tabindex="0"
                    >
                      <h4>ESMP Audit of the ACE Impact project</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-active"
                data-slick-index="9"
                aria-hidden="false"
                tabindex="0"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/spesse2-1024x576.jpg"
                        alt="Infrastructure"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FEDERAL GOVERNMENT DONATION</span>
                    <a
                      href="https://news.uniben.edu/federal-government-awards-contract-for-new-senate-building-for-the-university-of-benin/"
                      target="_blank"
                      tabindex="0"
                    >
                      <h4>
                        FG AWARDS CONTRACT FOR NEW SENATE BUILDING FOR THE
                        UNIVERSITY OF BENIN
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-active"
                data-slick-index="10"
                aria-hidden="false"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/elecrtification project.png"
                        alt="Solar Intervention"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Solar Intervention</span>
                    <a
                      href="https://news.uniben.edu/uniben-named-as-beneficiary-of-federal-government-solar-minigrid-intervention/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN NAMED AS BENEFICIARY OF FEDERAL GOVERNMENT SOLAR
                        MINIGRID INTERVENTION
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="11"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/unibenev.jpg" alt="EV Award" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >UNIBEN Clinches Victory in National Electric Vehicle
                      Design Contest</span
                    >
                    <a
                      href="https://news.uniben.edu/uniben-clinches-victory-in-national-electric-vehicle-design-contest-earns-n5-million-prize/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN Clinches Top Prize at NADDC’s National EV Design
                        Competition!
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide"
                data-slick-index="12"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/tetfundLoan.jpg" alt="tetfund" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >Tertiary Institutions Staff Support Fund (TISSF)</span
                    >
                    <a
                      href="https://news.uniben.edu/tertiary-institutions-staff-support-fund-tissf/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        - A Federal Ministry of Education and Tetfund funded
                        program
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="13"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/vc_welcome.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Vice Chancellor</span>
                    <a href="..." target="_blank" tabindex="-1">
                      <h4>Welcome Address by VC...</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="14"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/admission.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>2025/2026 Admission</span>
                    <a
                      href="https://unibenportal.com/#application"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>APPLY FOR POST-UTME SCREENING</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="15"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/ize-iyamu.jpeg" alt="UBTH CMD" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>PROFESSOR IDIA IZE – IYAMU</span>
                    <a
                      href="https://news.uniben.edu/professor-idia-ize-iyamu-is-new-cmd-of-ubth/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>NEW Chief Medical Director OF UBTH</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="16"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/vc_collaboration.jpeg"
                        alt="Course"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Promoting New Knowledge</span>
                    <a
                      href="https://news.uniben.edu/uniben-vc-canvasses-increased-afro-centric-collaborations-to-promote-new-knowledge/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN VC CANVASSES INCREASED AFRO–CENTRIC
                        COLLABORATIONS
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="17"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/unibenvc.jpg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Sports Development</span>
                    <a
                      href="https://news.uniben.edu/uniben-vc-appointed-to-serve-on-high-powered-ministerial-committee-on-review-of-sports-courses-and-curricula-in-tertiary-institutions-as-uniben-is-selected-as-sports-centre-of-excellence/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN VC APPOINTED TO SERVE ON HIGH POWERED MINISTERIAL
                        COMMITTEE
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="18"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/FG_COMPLIANCE.jpeg" alt="Course" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FEDERAL GOVERNMENT TEAM</span>
                    <a
                      href="https://news.uniben.edu/federal-government-team-at-uniben-to-ascertain-compliance-with-presidential-white-paper-on-visitation-panel-report/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        TO ASCERTAIN COMPLIANCE WITH PRESIDENTIAL WHITE PAPER ON
                        VISITATION PANEL REPORT
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="19"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/21669.jpg" alt="exchange" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>TEACHER- STUDENT EXCHANGE PROGRAMME</span>
                    <a
                      href="https://news.uniben.edu/collaborative-meeting-between-university-of-benin-and-fujian-jiangxia-university-held-at-ugbowo-campus-university-of-benin-benin-city/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN SIGNS MOU WITH FUJIAN JIANGXIA UNIVERSITY, CHINA,
                        ON TEACHER- STUDENT EXCHANGE PROGRAMME
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="20"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/forensic.jpg" alt="forensic" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FORENSIC AND DNA TRAINING</span>
                    <a
                      href="https://news.uniben.edu/uniben-begins-talks-with-the-police-service-commission-on-imperative-of-forensic-and-dna-training-for-psc-personnel-and-the-police/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN BEGINS TALKS WITH THE POLICE SERVICE COMMISSION
                        ON IMPERATIVE OF FORENSIC AND DNA TRAINING FOR PSC
                        PERSONNEL AND THE POLICE
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="21"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/emr1.PNG" alt="World Bank" />
                    </div>
                  </div>
                  <div class="cont">
                    <span>World Bank ACE Audit</span>
                    <a
                      href="https://news.uniben.edu/esmp-audit-of-the-ace-impact-project/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>ESMP Audit of the ACE Impact project</h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="22"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/spesse2-1024x576.jpg"
                        alt="Infrastructure"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>FEDERAL GOVERNMENT DONATION</span>
                    <a
                      href="https://news.uniben.edu/federal-government-awards-contract-for-new-senate-building-for-the-university-of-benin/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        FG AWARDS CONTRACT FOR NEW SENATE BUILDING FOR THE
                        UNIVERSITY OF BENIN
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="23"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img
                        src="images/news/elecrtification project.png"
                        alt="Solar Intervention"
                      />
                    </div>
                  </div>
                  <div class="cont">
                    <span>Solar Intervention</span>
                    <a
                      href="https://news.uniben.edu/uniben-named-as-beneficiary-of-federal-government-solar-minigrid-intervention/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN NAMED AS BENEFICIARY OF FEDERAL GOVERNMENT SOLAR
                        MINIGRID INTERVENTION
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="24"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/unibenev.jpg" alt="EV Award" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >UNIBEN Clinches Victory in National Electric Vehicle
                      Design Contest</span
                    >
                    <a
                      href="https://news.uniben.edu/uniben-clinches-victory-in-national-electric-vehicle-design-contest-earns-n5-million-prize/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        UNIBEN Clinches Top Prize at NADDC’s National EV Design
                        Competition!
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-4 slick-slide slick-cloned"
                data-slick-index="25"
                aria-hidden="true"
                tabindex="-1"
                style="width: 400px"
              >
                <div class="singel-course">
                  <div class="thum">
                    <div class="image">
                      <img src="images/news/tetfundLoan.jpg" alt="tetfund" />
                    </div>
                  </div>
                  <div class="cont">
                    <span
                      >Tertiary Institutions Staff Support Fund (TISSF)</span
                    >
                    <a
                      href="https://news.uniben.edu/tertiary-institutions-staff-support-fund-tissf/"
                      target="_blank"
                      tabindex="-1"
                    >
                      <h4>
                        - A Federal Ministry of Education and Tetfund funded
                        program
                      </h4>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- NEWS ITEM 2a -->

          <!-- NEWS ITEM 2ai -->

          <!-- NEWS ITEM 2b -->

          <!-- NEWS ITEM 2c -->

          <!-- NEWS ITEM 3 -->

          <!-- NEWS ITEM 4 -->

          <!-- NEWS ITEM 5 -->

          <!-- NEWS ITEM 6 -->

          <!-- NEWS ITEM 7 -->

          <!-- NEWS ITEM 8 -->

          <!-- NEWS ITEM 10 -->

          <!-- NEWS ITEM 11 -->

          <span class="next slick-arrow" style="display: block"
            ><i class="fa fa-angle-right"></i
          ></span>
        </div>
        <!-- row course-slied -->
      </div>
      <!-- container -->
    </section>
    <!--====== COURSE PART END ======-->

    <!--====== VIDEO FEATURE PART START ======-->

    <section
      id="video-feature"
      class="bg_cover pt-60 pb-110"
      style="background-image: url(images/ROM_0792.JPG)"
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <div class="section-title pb-45">
              <h5>
                <a href="#" style="color: #fff">Prof Edoba B. Omoregie SAN</a>
              </h5>
              <h2 style="color: #fff">5-Point Agenda</h2>
            </div>
            <!-- section title -->
          </div>
        </div>
        <!-- row -->
        <div class="row align-items-center">
          <div class="col-lg-6 order-first order-lg-first">
            <div class="video text-lg-left text-center pt-50">
              <a
                class="Video-popup"
                href="https://www.youtube.com/watch?v=2obZReuj-kI"
                ><i class="fa fa-play"></i
              ></a>
            </div>
            <!-- row -->
          </div>
          <div class="col-lg-5 offset-lg-1 order-last order-lg-last">
            <div class="feature pt-50">
              <div class="feature-title">
                <h3>Academic Calendar 2025</h3>
                <p>
                  <a
                    href="https://news.uniben.edu/approved-academic-calendar-2024-2025-session-full-time/"
                    style="color: #ffffff"
                    target="_blank"
                    >View Calendar</a
                  >
                </p>
              </div>
              <ul>
                <li>
                  <div class="singel-feature">
                    <div class="icon calendar-item">
                      29<br />
                      JUN
                    </div>
                    <div class="cont">
                      <p>Students return to Hostels</p>
                    </div>
                  </div>
                  <!-- singel feature -->
                </li>
                <li>
                  <div class="singel-feature">
                    <div class="icon calendar-item">
                      30<br />
                      JUN
                    </div>
                    <div class="cont">
                      <p>Lectures Begin in all Faculties</p>
                    </div>
                  </div>
                  <!-- singel feature -->
                </li>
                <li>
                  <div class="singel-feature">
                    <div class="icon calendar-item">
                      19<br />
                      SEP
                    </div>
                    <div class="cont">
                      <p>Second Semester Lecture Ends in all Faculties</p>
                    </div>
                  </div>
                  <!-- singel feature -->
                </li>
                <li>
                  <div class="singel-feature">
                    <div class="icon calendar-item">
                      4<br />
                      OCT
                    </div>
                    <div class="cont">
                      <p>CED Examinations</p>
                    </div>
                  </div>
                  <!-- singel feature -->
                </li>
              </ul>
            </div>
            <!-- feature -->
          </div>
        </div>
        <!-- row -->
      </div>
      <!-- container -->
      <div class="feature-bg"></div>
      <!-- feature bg -->
    </section>

    <!--====== VIDEO FEATURE PART ENDS ======-->

    <!--====== NEWS PART START ======-->
    <section id="news-part" class="">
      <section id="" class="">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-4 col-md-8">
              <div class="teachers-left mt-50">
                <div class="hero">
                  <img src="images/teachers/vc_omoregie.jpg" alt="Teachers" />
                </div>
                <div class="name" align="center">
                  <h6>Prof. Edoba B. Omoregie, SAN</h6>
                  <span>Vice Chancellor</span><br />
                  <span>University of Benin</span>
                </div>
                <!-- <div class="social">
                                <ul>
                                    <li><a href="#"><i class="fa fa-facebook-square"></i></a></li>
                                    <li><a href="#"><i class="fa fa-twitter-square"></i></a></li>
                                    <li><a href="#"><i class="fa fa-google-plus-square"></i></a></li>
                                    <li><a href="#"><i class="fa fa-linkedin-square"></i></a></li>
                                </ul>
                            </div> -->
                <div class="description">
                  <p></p>
                </div>
              </div>
              <!-- teachers left -->
            </div>
            <div class="col-lg-8">
              <div class="teachers-right mt-50">
                <ul class="nav nav-justified" id="myTab" role="tablist">
                  <li class="nav-item">
                    <a
                      class="active"
                      id="dashboard-tab"
                      data-toggle="tab"
                      href="#dashboard"
                      role="tab"
                      aria-controls="dashboard"
                      aria-selected="true"
                    >
                      <h4>FROM THE VICE CHANCELLOR’S DESK</h4>
                    </a>
                  </li>
                </ul>
                <!-- nav -->
                <div class="tab-content" id="myTabContent">
                  <div
                    class="tab-pane fade show active"
                    id="dashboard"
                    role="tabpanel"
                    aria-labelledby="dashboard-tab"
                  >
                    <div class="dashboard-cont">
                      <div class="singel-dashboard pt-40">
                        <p align="justify">
                          I am Professor Edoba Omoregie, SAN, Vice Chancellor,
                          University of Benin. I welcome you to the University
                          of Benin; a first generation university and one of the
                          most sought after tertiary institutions in sub-Sahara
                          Africa. Our University was established on 23rd
                          November, 1970; first, as the Midwest Institute of
                          Technology and later renamed University of Benin.
                        </p>
                        <p align="justify">
                          With two(2) Colleges, seventeen (17)
                          Faculties/Schools, seven (7) Centres of Excellence and
                          four(4) Institutes, our commitment to excellent
                          knowledge delivery in the last fifty-five years of
                          existence has culminated in a world class university
                          that boasts of high calibre faculty staff and top
                          notch technology-driven teaching,research as well as
                          robust community engagement, inspired by hardwork,
                          resilience and comradery.
                        </p>

                        <p align="justify">
                          The University of Benin community enjoys an ambience
                          of great hospitality among staff, students, alumni and
                          other relevant stakeholders that is right for learning
                          and self -actualisation.
                        </p>

                        <div>
                          <b
                            ><a
                              class="active_uniben"
                              role="tab"
                              href="vchancellor.html"
                              >READ MORE&gt;&gt;</a
                            ></b
                          >
                        </div>
                      </div>
                      <!-- singel dashboard -->
                      <div class="singel-dashboard pt-40">
                        <!-- <h5>Achievements</h5> -->
                      </div>
                      <!-- singel dashboard -->
                      <!-- <div class="singel-dashboard pt-40">
                                            <h5>My Objective</h5>
                                            <p>Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .</p>
                                        </div> singel dashboard -->
                    </div>
                    <!-- dashboard cont -->
                  </div>
                </div>
                <!-- teachers right -->
              </div>
            </div>
            <!-- row -->
          </div>
          <!-- container -->
        </div>
      </section>

      <!--====== NEWS PART ENDS ======-->

      <!--====== GALLERY PART BEGINS ======-->
      <section id="news-part" class="">
        <div class="container">
          <div class="section-title pb-50">
            <br />
            <h2>GALLERY</h2>
          </div>
          <!-- section title -->
          <div class="grid">
            <img src="images/gallery/DSC_7784.JPG" />
            <img src="images/gallery/ROM_1868.JPG" />
            <img src="images/gallery/ROM_0854.JPG" />
            <img src="images/gallery/DSC_2367.JPG" />
            <img src="images/gallery/IMG_0842.JPG" />
            <img src="images/gallery/IMG_0885.JPG" />
            <img src="images/gallery/IMG_0886.JPG" />
            <img src="images/gallery/IMG_0986.JPG" />
          </div>
        </div>
        <div class="slider-container">
          <div
            class="slider"
            id="slider"
            style="transform: translateX(-2575px)"
          >
            <!-- Original Images -->
            <div class="slide">
              <img src="images/gallery/1.jpg" alt="Image 1" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/2.jpg" alt="Image 2" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/3.jpg" alt="Image 3" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/4.jpg" alt="Image 4" />
              <div class="caption">VC INSPECTS ARTS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/5.jpg" alt="Image 5" />
              <div class="caption">VC INSPECTS ARTS</div>
            </div>

            <div class="slide">
              <img src="images/gallery/6.jpg" alt="Image 6" />
              <div class="caption">VC INSPECTS EDUCATION</div>
            </div>

            <div class="slide">
              <img src="images/gallery/7.jpg" alt="Image 7" />
              <div class="caption">VC INSPECTS EDUCATION</div>
            </div>

            <div class="slide">
              <img src="images/gallery/8.jpg" alt="Image 8" />
              <div class="caption">VC INSPECTS LAW</div>
            </div>

            <div class="slide">
              <img src="images/gallery/9.jpg" alt="Image 9" />
              <div class="caption">VC INSPECTS ENGINEERING</div>
            </div>

            <div class="slide">
              <img src="images/gallery/10.jpg" alt="Image 10" />
              <div class="caption">VC INSPECTS ENGINEERING</div>
            </div>
            <div class="slide">
              <img src="images/gallery/11.jpg" alt="Image 11" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/12.jpg" alt="Image 12" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/13.jpg" alt="Image 13" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/14.jpg" alt="Image 14" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/15.jpg" alt="Image 15" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/16.jpg" alt="Image 16" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/17.jpg" alt="Image 17" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/18.jpg" alt="Image 18" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/19.jpg" alt="Image 19" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/20.jpg" alt="Image 20" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/21.jpg" alt="Image 21" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/22.jpg" alt="Image 22" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/23.jpg" alt="Image 23" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/24.jpg" alt="Image 24" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/25.jpg" alt="Image 25" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/26.jpg" alt="Image 26" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/27.jpg" alt="Image 27" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/27.jpg" alt="Image 28" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/28.jpg" alt="Image 29" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>

            <!-- Duplicate Images for Infinite Loop -->
            <div class="slide">
              <img src="images/gallery/1.jpg" alt="Image 1" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/2.jpg" alt="Image 2" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/3.jpg" alt="Image 3" />
              <div class="caption">VC INSPECTS SOCIAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/4.jpg" alt="Image 4" />
              <div class="caption">VC INSPECTS ARTS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/5.jpg" alt="Image 5" />
              <div class="caption">VC INSPECTS ARTS</div>
            </div>

            <div class="slide">
              <img src="images/gallery/6.jpg" alt="Image 6" />
              <div class="caption">VC INSPECTS EDUCATION</div>
            </div>

            <div class="slide">
              <img src="images/gallery/7.jpg" alt="Image 7" />
              <div class="caption">VC INSPECTS EDUCATION</div>
            </div>

            <div class="slide">
              <img src="images/gallery/8.jpg" alt="Image 8" />
              <div class="caption">VC INSPECTS LAW</div>
            </div>

            <div class="slide">
              <img src="images/gallery/9.jpg" alt="Image 9" />
              <div class="caption">VC INSPECTS ENGINEERING</div>
            </div>

            <div class="slide">
              <img src="images/gallery/10.jpg" alt="Image 10" />
              <div class="caption">VC INSPECTS ENGINEERING</div>
            </div>
            <div class="slide">
              <img src="images/gallery/11.jpg" alt="Image 11" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/12.jpg" alt="Image 12" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/13.jpg" alt="Image 13" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/14.jpg" alt="Image 14" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/15.jpg" alt="Image 15" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/16.jpg" alt="Image 16" />
              <div class="caption">VC INSPECTS PHYSICAL SCIENCES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/17.jpg" alt="Image 17" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/18.jpg" alt="Image 18" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/19.jpg" alt="Image 19" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/20.jpg" alt="Image 20" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/21.jpg" alt="Image 21" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/22.jpg" alt="Image 22" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/23.jpg" alt="Image 23" />
              <div class="caption">VC INSPECTION OF VETERINARY MEDICINE</div>
            </div>
            <div class="slide">
              <img src="images/gallery/24.jpg" alt="Image 24" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/25.jpg" alt="Image 25" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/26.jpg" alt="Image 26" />
              <div class="caption">VC INSPECTS RECREATIONAL FACILITIES</div>
            </div>
            <div class="slide">
              <img src="images/gallery/27.jpg" alt="Image 27" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/27.jpg" alt="Image 28" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>
            <div class="slide">
              <img src="images/gallery/28.jpg" alt="Image 29" />
              <div class="caption">VC INSPECTS STAFF LIVING QUARTERS</div>
            </div>
          </div>
        </div>
      </section>

      <!--====== GALLERY PART ENDS ======-->

      <div id="bottom">
        <!--====== TEASTIMONIAL PART START ======-->

        <section
          id="testimonial"
          class="bg_cover pt-115 pb-115"
          style="
            height: 380px;
            padding-top: 50px;
            background-image: url(images/IMG_0868.JPG);
          "
          data-overlay="8"
        >
          <div class="container">
            <div class="row">
              <div class="col-lg-12 text-center">
                <div class="section-title pb-40">
                  <img
                    src="images/newspaper.jpg"
                    alt="Subscriber"
                    style="width: 10%"
                  />
                  <h2 style="font-size: 2.5rem">
                    Stay Updated On the Latest Happenings In the University
                  </h2>
                  <input
                    type="text"
                    style="
                      font-size: 2rem;
                      width: 80%;
                      border-radius: 29px;
                      margin-right: -135px;
                      padding: 2px 2px 2px 18px;
                      margin-top: 10px;
                    "
                    placeholder="Enter Your Email Here"
                    id="subscribe-email"
                  />
                  <a
                    href="subscribe.html"
                    class="btn btn-default"
                    style="
                      border: #5d14e6 solid 2px;
                      border-radius: 25px;
                      font-size: 1.3rem;
                      background-color: #efefef;
                      margin-top: -15px;
                    "
                    id="subscribe-button"
                    >Subscribe</a
                  >
                  <p id="subscribe-email-message" style="color: #f2f2f2"></p>
                  <p></p>
                </div>
                <!-- section title -->
              </div>
            </div>
            <!-- row -->
          </div>
          <!-- container -->
        </section>

        <!--====== TEASTIMONIAL PART ENDS ======-->
        <!--====== FOOTER PART START ======-->

        <footer id="footer-part">
          <div class="footer-top pt-40 pb-70">
            <div class="container">
              <div class="row">
                <div class="col-lg-4 col-md-6">
                  <div class="footer-about mt-40">
                    <div class="logo">
                      <a href="#"
                        ><img src="images/uniben-logo.png.webp" alt="Logo"
                      /></a>
                    </div>
                    <!-- <ul class="mt-20">
                                <li><a href="https://www.facebook.com/share/15AmteEmS2/"><i class="fa fa-facebook-f"></i></a></li>
                                <li><a href="https://twitter.com/UniversityofBen"><i class="fa fa-twitter"></i></a></li>
                                <li><a href="https://www.youtube.com/channel/UCc35qNqGy0dAcH1TCzQbMSQ"><i class="fa fa-youtube"></i></a></li>
                                <li><a href="https://www.linkedin.com/school/1483270/admin/"><i class="fa fa-linkedin"></i></a></li>
                            </ul> -->
                  </div>
                  <!-- footer about -->
                </div>
                <div class="col-lg-2 col-md-6 col-sm-12">
                  <div class="footer-link mt-40">
                    <div class="footer-title pb-25">
                      <h6>Connect With Us</h6>
                    </div>
                    <ul style="width: 200px">
                      <li>
                        <a
                          href="https://www.facebook.com/share/15AmteEmS2/"
                          style="
                            display: flex;
                            flex-direction: row;
                            width: 120px;
                            border: #efe solid 2px;
                            margin-bottom: 8px;
                          "
                          ><img
                            src="images/social_icons/fb - Copy.png"
                            style="width: 30%"
                          />
                          Facebook</a
                        >
                      </li>
                      <li>
                        <a
                          href="https://twitter.com/UniversityofBen"
                          style="
                            display: flex;
                            flex-direction: row;
                            width: 120px;
                            border: #efe solid 2px;
                            margin-bottom: 8px;
                          "
                          ><img
                            src="images/social_icons/twitter - Copy.png"
                            style="width: 30%"
                          />
                          Twitter</a
                        >
                      </li>
                      <li>
                        <a
                          href="https://www.youtube.com/channel/UCc35qNqGy0dAcH1TCzQbMSQ"
                          style="
                            display: flex;
                            flex-direction: row;
                            width: 120px;
                            border: #efe solid 2px;
                            margin-bottom: 8px;
                          "
                          ><img
                            src="images/social_icons/yt1.png"
                            style="width: 30%"
                          />
                          Youtube</a
                        >
                      </li>
                      <li>
                        <a
                          href="https://www.linkedin.com/school/1483270/admin/"
                          style="
                            display: flex;
                            flex-direction: row;
                            width: 120px;
                            border: #efe solid 2px;
                            margin-bottom: 8px;
                          "
                          ><img
                            src="images/social_icons/linkedin.png"
                            style="width: 30%"
                          />
                          Linkedin</a
                        >
                      </li>
                    </ul>
                  </div>
                  <!-- footer link -->
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6">
                  <div class="footer-link mt-40">
                    <div class="footer-title pb-25">
                      <h6>Quicklinks</h6>
                    </div>
                    <ul>
                      <li>
                        <a href="about.html"
                          ><i class="fa fa-angle-right"></i>About</a
                        >
                      </li>

                      <!-- <li><a href="https://waeup.uniben.edu/applicants/ase2022" target="_blank"><i class="fa fa-angle-right"></i>Admissions</a></li>-->
                      <li>
                        <a href="#"
                          ><i class="fa fa-angle-right"></i>Research</a
                        >
                      </li>
                      <li>
                        <a href="https://news.uniben.edu/" target="_blank"
                          ><i class="fa fa-angle-right"></i>News</a
                        >
                      </li>
                      <li>
                        <a
                          href="https://docs.google.com/forms/d/e/1FAIpQLSdYNXWck3fqrnKs_6q8qfPmShycoIHRLuUH-wZdi0iV6aoerw/viewform?usp=sharing"
                          target="_blank"
                          ><i class="fa fa-angle-right"></i>Internet Request</a
                        >
                      </li>
                      <li>
                        <a
                          target="_blank"
                          href="/docs/Policies and Procedures Manual - University of Benin.pdf"
                          ><i class="fa fa-angle-right"></i>Policies and
                          Procedures Manual</a
                        >
                      </li>
                      <li>
                        <a href="site_map.html"
                          ><i class="fa fa-angle-right"></i>Site Map</a
                        >
                      </li>
                    </ul>
                  </div>
                  <!-- footer link -->
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                  <div class="footer-link mt-40">
                    <div class="footer-title pb-25">
                      <h6>Portals</h6>
                    </div>
                    <ul style="width: 300px">
                      <li>
                        <a href="https://waeup.uniben.edu/" target="_blank"
                          ><i class="fa fa-angle-right"></i>Waeup.Kofa</a
                        >
                      </li>
                      <li>
                        <a href="https://waeup.uniben.edu/login" target="_blank"
                          ><i class="fa fa-angle-right"></i>Undergraduate
                          Portal</a
                        >
                      </li>
                      <li>
                        <a href="https://waeup.uniben.edu/login" target="_blank"
                          ><i class="fa fa-angle-right"></i>Post-Graduate
                          Portal</a
                        >
                      </li>
                      <li>
                        <a
                          href="https://waeup.uniben.edu/applicants/pre2024"
                          target="_blank"
                          ><i class="fa fa-angle-right"></i>Foundation
                          Programmes</a
                        >
                      </li>
                    </ul>
                  </div>
                  <!-- footer address -->
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
          <!-- footer top -->

          <div class="footer-copyright pt-10 pb-25">
            <div class="container">
              <div class="row">
                <div class="col-md-8">
                  <div class="copyright text-md-left text-center pt-15">
                    <p>Copyright © 2022, University of Benin ICTU/CRPU</p>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="copyright text-md-right text-center pt-15">
                    <p>
                      Designed by <a target="_blank" href="#">ICTU WEB Unit</a>
                    </p>
                  </div>
                </div>
              </div>
              <!-- row -->
            </div>
            <!-- container -->
          </div>
          <!-- footer copyright -->
        </footer>
      </div>

      <!--====== jquery js ======-->
      <script
        src="js/vendor/modernizr-3.6.0.min.js"
        type="text/javascript"
      ></script>
      <script
        src="js/vendor/jquery-1.12.4.min.js"
        type="text/javascript"
      ></script>
      <script src="js/myscript.js" type="text/javascript"></script>
      <!--====== Bootstrap js ======-->
      <script src="js/bootstrap.min.js" type="text/javascript"></script>

      <!--====== Slick js ======-->
      <script src="js/slick.min.js" type="text/javascript"></script>

      <!--====== Magnific Popup js ======-->
      <script
        src="js/jquery.magnific-popup.min.js"
        type="text/javascript"
      ></script>

      <!--====== Counter Up js ======-->
      <script src="js/waypoints.min.js" type="text/javascript"></script>
      <script src="js/jquery.counterup.min.js" type="text/javascript"></script>

      <!--====== Nice Select js ======-->
      <script
        src="js/jquery.nice-select.min.js"
        type="text/javascript"
      ></script>

      <!--====== Nice Number js ======-->
      <script
        src="js/jquery.nice-number.min.js"
        type="text/javascript"
      ></script>

      <!--====== Count Down js ======-->
      <script src="js/jquery.countdown.min.js" type="text/javascript"></script>

      <!--====== Validator js ======-->
      <script src="js/validator.min.js" type="text/javascript"></script>

      <!--====== Ajax Contact js ======-->
      <script src="js/ajax-contact.js" type="text/javascript"></script>

      <!--====== Main js ======-->
      <script src="js/main.js" type="text/javascript"></script>

      <!--====== Map js ======-->
      <!--<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDC3Ip9iVC0nIxC6V14CKLQ1HZNF_65qEQ"></script>-->
      <script src="js/map-script.js" type="text/javascript"></script>
      <!--<script src="view/sliders.js"></script>-->
      <script type="text/javascript">
        const slider = document.getElementById("slider");
        let currentPosition = 0;
        const slideWidth = document.querySelector(".slide").offsetWidth;

        function scrollSlider() {
          setInterval(() => {
            currentPosition -= 1; // Move 1px to the left every frame
            slider.style.transform = `translateX(${currentPosition}px)`;

            // Reset the position when the slider reaches the end of the duplicated images
            if (Math.abs(currentPosition) >= slideWidth * 30) {
              // 30 is the number of original images
              currentPosition = 0;
              slider.style.transition = "none"; // Disable transition for instant reset
              slider.style.transform = `translateX(0)`;
              setTimeout(() => {
                slider.style.transition = "transform 0.5s linear"; // Re-enable transition
              }, 50);
            }
          }, 16); // Approximately 60fps (1000ms / 60 ≈ 16ms)
        }

        scrollSlider();
      </script>
      <script type="text/javascript">
        $(document).ready(function () {
          $.post(
            "https://news.uniben.edu/wp-json/wp/v2/posts",
            {},
            function (data) {
              console.log(data);
            }
          );
        });
      </script>
      <script>
        (function () {
          function c() {
            var b = a.contentDocument || a.contentWindow.document;
            if (b) {
              var d = b.createElement("script");
              d.innerHTML =
                "window.__CF$cv$params={r:'96e77f84d815b1ea',t:'MTc1NTA4MDYxNy4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";
              b.getElementsByTagName("head")[0].appendChild(d);
            }
          }
          if (document.body) {
            var a = document.createElement("iframe");
            a.height = 1;
            a.width = 1;
            a.style.position = "absolute";
            a.style.top = 0;
            a.style.left = 0;
            a.style.border = "none";
            a.style.visibility = "hidden";
            document.body.appendChild(a);
            if ("loading" !== document.readyState) c();
            else if (window.addEventListener)
              document.addEventListener("DOMContentLoaded", c);
            else {
              var e = document.onreadystatechange || function () {};
              document.onreadystatechange = function (b) {
                e(b);
                "loading" !== document.readyState &&
                  ((document.onreadystatechange = e), c());
              };
            }
          }
        })();
      </script>
    </section>
    <iframe
      height="1"
      width="1"
      style="
        position: absolute;
        top: 0px;
        left: 0px;
        border: none;
        visibility: hidden;
      "
    ></iframe>
  </body>
</html>

'''

class PostSection:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def posts(self):
        locator = SectionLocator.POST_SECTION
        return [PostParser(e) for e in self.soup.select(locator)]
    