job_board_html = """
<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Jobpy Board</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="has-animations">
<div class="body-wrap">
    <header class="site-header reveal-from-bottom">
        <div class="container">
            <div class="site-header-inner">
                <div class="brand"><h1 class="m-0"><a href="index.html"><img src="images/logo.svg" alt="Storm"
                                                                             width="32" height="32"></a></h1></div>
                <button id="header-nav-toggle" class="header-nav-toggle" aria-controls="primary-menu"
                        aria-expanded="false"><span class="screen-reader">Menu</span> <span class="hamburger"><span
                        class="hamburger-inner"></span></span></button>
                <nav id="header-nav" class="header-nav">
                    <div class="header-nav-inner">
                        <ul class="list-reset text-xxs header-nav-right">
                            <!--                            <li><a href="additional.html">Secondary page</a></li>-->
                        </ul>
                        <ul class="list-reset header-nav-right">
                            <!--                            <li><a class="button button-primary button-wide-mobile button-sm" href="signup.html">Sign-->
                            <!--                                up</a></li>-->
                        </ul>
                    </div>
                </nav>
            </div>
        </div>
    </header>
    <main class="site-content">
        <section class="hero section center-content illustration-section-01">
            <div class="container-sm">
                <div class="hero-inner section-inner">
                    <div class="hero-content"><h1 class="mt-0 mb-16 reveal-from-bottom" data-reveal-delay="200">
                        Tech-related jobs below.
                    </h1>
                        <div class="container-xs"><p class="mt-0 mb-32 reveal-from-bottom" data-reveal-delay="400">
                            The is a collection of tech-related jobs below. Feel free to scroll through and apply to you
                            heart's content.
                            Please note the date when this was last updated below.<br>
                            Last Updated: {Date}
                        </p>
                            <div class="reveal-from-bottom" data-reveal-delay="600">
                                <!--                                <a class="button button-primary" href="#">Get started</a></div>-->
                            </div>
                        </div>
                        <div class="hero-figure illustration-element-01 reveal-from-bottom" data-reveal-value="20px"
                             data-reveal-delay="800"><img src="images/hero-image.png" alt="Hero image"></div>
                    </div>
                </div>
        </section>
        <section class="features-tiles section center-content illustration-section-02">
            <div class="container">
                <div class="features-tiles-inner section-inner">
                    <div class="tiles-wrap">
                        <div class="tiles-item reveal-scale-up">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-01.svg" alt="Feature tile icon 01"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                        <div class="tiles-item reveal-scale-up" data-reveal-delay="200">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-02.svg" alt="Feature tile icon 02"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                        <div class="tiles-item reveal-scale-up" data-reveal-delay="400">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-03.svg" alt="Feature tile icon 03"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                        <div class="tiles-item reveal-scale-up">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-04.svg" alt="Feature tile icon 04"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                        <div class="tiles-item reveal-scale-up" data-reveal-delay="200">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-05.svg" alt="Feature tile icon 05"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                        <div class="tiles-item reveal-scale-up" data-reveal-delay="400">
                            <div class="tiles-item-inner">
                                <div class="features-tiles-item-header">
                                    <div class="features-tiles-item-image mb-16"><img
                                            src="images/feature-tile-icon-06.svg" alt="Feature tile icon 06"></div>
                                </div>
                                <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">User friendly</h4>
                                    <p class="m-0 text-sm">A pseudo-Latin text used in web design, layout, and printing
                                        in place of things to emphasise design.</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="testimonial section center-content illustration-section-07">
            <div class="container-xs">
                <div class="testimonial-inner section-inner">
                    <div class="tiles-wrap carousel-items reveal-scale-up" data-autorotate="7000">
                        <div class="tiles-item carousel-item">
                            <div class="tiles-item-inner">
                                <div class="testimonial-item-header mb-16">
                                    <div class="testimonial-item-image"><img src="images/JeffBezos.jpg"
                                                                             alt="Testimonial image 01" width="56"
                                                                             height="56"></div>
                                </div>
                                <div class="testimonial-item-content"><p class="m-0">What we need to do is always lean
                                    into the future; when the world changes around you and when it changes against you –
                                    what used to be a tail wind is now a head wind – you have to lean into that and
                                    figure out what to do because complaining isn’t a strategy.” – Jeff Bezos</p></div>
                            </div>
                        </div>
                        <div class="tiles-item carousel-item">
                            <div class="tiles-item-inner">
                                <div class="testimonial-item-header mb-16">
                                    <div class="testimonial-item-image"><img src="images/elon_musk.jpg"
                                                                             alt="Testimonial image 02" width="56"
                                                                             height="56"></div>
                                </div>
                                <div class="testimonial-item-content"><p class="m-0">“People work better when they know
                                    what the goal is and why. It is important that people look forward to coming to work
                                    in the morning and enjoy working.” - Elon Musk</p></div>
                            </div>
                        </div>
                        <div class="tiles-item carousel-item">
                            <div class="tiles-item-inner">
                                <div class="testimonial-item-header mb-16">
                                    <div class="testimonial-item-image"><img src="images/Steve-Jobs-1440x960.jpg"
                                                                             alt="Testimonial image 03" width="56"
                                                                             height="56"></div>
                                </div>
                                <div class="testimonial-item-content"><p class="m-0">“You can’t connect the dots looking
                                    forward; you can only connect them looking backwards. So you have to trust that the
                                    dots will somehow connect in your future. You have to trust in something — your gut,
                                    destiny, life, karma, whatever. This approach has never let me down, and it has made
                                    all the difference in my life.” — Steve Jobs.</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="site-footer center-content-mobile illustration-section-09">
        <div class="container">
            <div class="site-footer-inner has-top-divider">
                <div class="footer-top space-between text-xxs">
                    <div class="brand"><a href="index.html"><img src="images/logo.svg" alt="Storm" width="32"
                                                                 height="32"></a></div>
                    <div class="footer-social">
                        <ul class="list-reset">
                            <!--                            <li><a href="#">-->
                            <!--                                <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">-->
                            <!--                                    <title>Facebook</title>-->
                            <!--                                    <path d="M6.023 16L6 9H3V6h3V4c0-2.7 1.672-4 4.08-4 1.153 0 2.144.086 2.433.124v2.821h-1.67c-1.31 0-1.563.623-1.563 1.536V6H13l-1 3H9.28v7H6.023z"/>-->
                            <!--                                </svg>-->
                            <!--                            </a></li>-->
                            <li><a href="#">
                                <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                                    <title>Twitter</title>
                                    <path d="M16 3c-.6.3-1.2.4-1.9.5.7-.4 1.2-1 1.4-1.8-.6.4-1.3.6-2.1.8-.6-.6-1.5-1-2.4-1-1.7 0-3.2 1.5-3.2 3.3 0 .3 0 .5.1.7-2.7-.1-5.2-1.4-6.8-3.4-.3.5-.4 1-.4 1.7 0 1.1.6 2.1 1.5 2.7-.5 0-1-.2-1.5-.4C.7 7.7 1.8 9 3.3 9.3c-.3.1-.6.1-.9.1-.2 0-.4 0-.6-.1.4 1.3 1.6 2.3 3.1 2.3-1.1.9-2.5 1.4-4.1 1.4H0c1.5.9 3.2 1.5 5 1.5 6 0 9.3-5 9.3-9.3v-.4C15 4.3 15.6 3.7 16 3z"/>
                                </svg>
                            </a></li>
                            <!--                            <li><a href="#">-->
                            <!--                                <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">-->
                            <!--                                    <title>Instagram</title>-->
                            <!--                                    <g>-->
                            <!--                                        <circle cx="12.145" cy="3.892" r="1"/>-->
                            <!--                                        <path d="M8 12c-2.206 0-4-1.794-4-4s1.794-4 4-4 4 1.794 4 4-1.794 4-4 4zm0-6c-1.103 0-2 .897-2 2s.897 2 2 2 2-.897 2-2-.897-2-2-2z"/>-->
                            <!--                                        <path d="M12 16H4c-2.056 0-4-1.944-4-4V4c0-2.056 1.944-4 4-4h8c2.056 0 4 1.944 4 4v8c0 2.056-1.944 4-4 4zM4 2c-.935 0-2 1.065-2 2v8c0 .953 1.047 2 2 2h8c.935 0 2-1.065 2-2V4c0-.935-1.065-2-2-2H4z"/>-->
                            <!--                                    </g>-->
                            <!--                                </svg>-->
                            <!--                            </a></li>-->
                        </ul>
                    </div>
                </div>
                <div class="footer-bottom space-between text-xxs invert-order-desktop">
                    <nav class="footer-nav">
                        <!--                        <ul class="list-reset">-->
                        <!--                            <li><a href="#">Contact</a></li>-->
                        <!--                            <li><a href="#">About us</a></li>-->
                        <!--                            <li><a href="#">FAQ's</a></li>-->
                        <!--                            <li><a href="#">Support</a></li>-->
                        <!--                        </ul>-->
                    </nav>
                    <div class="footer-copyright">&copy; 2020 Jobpy, all rights reserved</div>
                </div>
            </div>
        </div>
    </footer>
</div>
<script src="js/main.min.js"></script>
</body>
</html>
"""

try:
    from search.cb_job_search import start_search, grab_jobs_links, get_job_information
except ImportError:
    print('Module "search" from Jobpy was not imported correctly.')

if __name__ == '__main__':
    for job_link in grab_jobs_links("Python Developer", "Pennsylvania"):
        job_data = get_job_information(job_link)

        clean_job_data = ''.join(job_data["Description"]).strip()
        clean_job_skills = ', '. join(job_data["Skills"])

        div = f"""
        <div class="features-tiles-item-content"><h4 class="mt-0 mb-8">{job_data["Job Title"]}|{job_data["Company"]}|{job_data["Location"]}</h4>
        <p class="m-0 text-sm"></p></div>
        <p class="m-0 text-sm">{clean_job_data[:clean_job_data.find("Recommended skills")]}</p></div>
        <p class="m-0 text-sm">{clean_job_skills}</p></div>
        """

        print(div)

        break
