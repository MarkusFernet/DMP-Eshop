import React from 'react';

function HomePage() {
  return (
    <>
      <section className="text-center container">
        <div className="row py-lg-3">
          <div className="col-lg-6 col-md-8 mx-auto">
            <h1 className="h1 fw-bold">Nadpis</h1>
            <p className="lead text-muted sansserif">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget
              porttitor ex. In hac habitasse platea dictumst. Sed ut sapien et lectus molestie efficitur sed sed
              libero. Vestibulum quis bibendum felis. Morbi semper metus sit amet felis faucibus porta. Cras venenatis
              augue eu imperdiet dignissim. Suspendisse sed tempus neque. Vivamus quis sodales nunc, ut ultrices arcu.
              Aliquam erat volutpat. Phasellus vitae augue semper, rutrum nulla sed, sollicitudin justo. In eu
              tristique nibh, ac aliquam odio. Phasellus blandit dui ut libero rutrum, nec bibendum quam bibendum.
              Aliquam tellus est, hendrerit eget fringilla vitae, efficitur vel nunc.</p>
            <p>
              <a href="#" className="btn btn-primary my-2">Tlačítko</a>
            </p>
          </div>
        </div>
      </section>
      <div className="container">
        <div className="row">
          <div className="album pt-5">
            <div className="col-12 pb-3">
              <h1 className="h3">Nejpopulárnější produkty</h1>
            </div>
            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-5 g-3">
              <div className="col">
                <div className="card shadow-sm">
                  <a href="#">
                    <img className="img-fluid" src="#" alt="Product Image" />
                  </a>
                  <div className="card-body">
                    <p className="card-text">
                      <a className="text-dark text-decoration-none" href="#">Product Title</a>
                    </p>
                    <div className="fw-bold">Product Price</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default HomePage;