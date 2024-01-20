# Sanda Bazaar
*A Treasure Trove on Gotland*

![Project Image](readme/biglogo50.webp))
<hr>

<h3 align="center">Full-Stack Project- E-Commerce(HTML5, CSS3, Bootstrap, Django, Python, JavaScript, jQuery, PostgreSQL, AWS, Heroku)
</h3>

**TABLE OF CONTENTS**

  - [Overview](#overview)
  - [UX](#ux)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Surface](#surface)
  - [Business Model](#business-model)
  - [Marketing](#marketing)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
  - [Database](#database)
  - [Responsive Layout and Design](#responsive-layout-and-design)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)

## Overview
Sanda Bazaar is an e-commerce platform that merges the distinctive charm of Gotland's culture with the convenience of online shopping. Our mission is to streamline the buying process for a wide array of culturally rich products. Customers have the ability to delve into product details, curate wishlists, place items into their shopping carts, and complete transactions through secure online payments. The site additionally facilitates order history tracking for enhanced user convenience.

Developed with a robust tech stack comprising Python, Django, HTML, CSS, and JavaScript, Sanda Bazaar provides a seamless and engaging user experience. The platform's performance is anchored by a PostgreSQL database, ensuring reliability and efficiency in data management.

A unique feature of Sanda Bazaar is our summer shop. Nestled in the heart of Gotland, the summer shop offers a tranquil retreat for visitors. Here, they can enjoy a cup of coffee, indulge in light refreshments, and experience the local ambiance. The summer shop serves as a physical extension of our digital marketplace, allowing customers to immerse themselves in the tangible essence of Gotland's culture. It's a place where online shopping meets real-world experience, creating a complete and enriching journey into the world of diverse cultures.

Experience the essence of Gotland at Sanda Bazaar, where every purchase, whether online or at our summer shop, is a journey into a world of diverse cultures and unique experiences.
<br><br>
The fully deployed project can be accessed at [this link](https://thebazaar-30d8729d015c.herokuapp.com/).<br><br>

## UX

### Viewing and Navigation EPIC

- As a user, I want to understand the purpose of the website from the first interaction with the content.
- As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device.
- As a user, I want to see a footer with relevant information and documents.
- As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content.
- As a user, I want to be able search through site products by entering a key word.

### User Registration/Authentication EPIC

- As a user, I want to be able to register on the website.
- As a user, I want to be able to confirm my account with an email.
- As a user/admin, I want to be able to authenticate using only email and password.
- As a user, I want to be able to reset my password in case I forgot it.
- As a user/admin, I want to be able to log out at any time.

### Products EPIC

- As a user, I want to see a catalog with all the products and also grouped by categories.
- As a user, I want to be able to apply filters and to sort the listed products, so I can easily find the ones I am interested to buy.
- As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy.
- As a user, I want to be able to add any product to the shopping bag in a selected quantity.
- As an admin, I want to be able to edit product details.
- As an admin, I want to be able to delete products from the catalog.
- As an admin, I want to be able to add new products to catalog.

### Reviews EPIC

- As a user, I want to be able to see all the reviews added for any product, so I can easily make an opinion about its quality.
- As a logged in user, I want to be able to add a review for any product I have purchased.
- As a user, I want to be able to see a general rating of every product.

### Wishlist EPIC

- As a logged-in user, I want to be able to add/remove any product from the Wishlist.
- As a logged-in user, I want to see all the products added to Wishlist.

### Bag EPIC

- As a user, I want to see all the products I added to the shopping bag.
- As a user, I want to be able to add/remove any product from the shopping bag.
- As a user, I want to see all the details about the price for the order.
- As a user, I want to be able to edit the quantity of the products.

### Checkout EPIC

- As a logged-in user, I want to be able to see and edit my default delivery details for the order.
- As a user, I want to see the order summary with all the price details.
- As a user, I want to be able to add my delivery details for the order.
- As a user, I want to be able to introduce my card details for payment.

### User Profile EPIC

- As a logged in user, I want to be able to see and edit my delivery details.
- As a logged-in user, I want to be able to see my orders history.
- As a logged-in user, I want to see the full details for every order I placed on the website.

### Admin Manage Orders EPIC

- As an admin, I want to be able to see all the orders placed on the website grouped by date.
- As an admin, I want to be able to filter the orders by date.
- As an admin, I want to see full details of every order placed on the website.

### Newsletter EPIC

- As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions.
- As an admin, I can keep track of all our subscribers, and utilise it to keep our customers be up to date with the latest promotions, thereby using it as a marketing tool to increase revenue.

### About EPIC

- As a user, I want a clear link to the About page to learn about Sanda Bazaar.
- As a user, I want to see who's behind Sanda Bazaar, adding a personal touch.

### Contact EPIC

- As a user, I can easily navigate to the website's contact page.
- As a user, I can find the bazaar's location, opening hours, and contact number and email address.
- As a user, I can use the google map to locate the bazaar's exact location.
- As a user, I want easy access to contact info and social media links on the Contact page.

### Blog EPIC

- As a user, I want to easily find and access the blog page to explore topics related to Sanda Bazaar.
- As a user, I'm interested in reading diverse blog posts that cover a range of topics from cultural insights to behind-the-scenes stories of the bazaar.
- As a user, I want the blog to feature engaging and well-written content that captures my interest and keeps me coming back for more.
- As a user, I'm looking for visually appealing blog posts, with images or videos that enhance the storytelling.

### FAQs Page EPIC

- As a user, I can easily navigate to the website's FAQs page.
- As a user, I can get all the answers to

### Project Goal
Develop a user-friendly online shopping experience for Sanda Bazaar, catering to both customers and staff efficiently.

[Back to top ⇧](#overview)

## Scope

### Project Objectives
- Create a user-intuitive website interface.
- Incorporate content enhancing Sanda Bazaar's brand and appeal.
- Clearly separate functionalities for customer and staff accounts.
- Introduce features to streamline staff operations and enrich customer shopping experience, including product organization, operational hours, and a blog for updates.
- Ensure compatibility and responsiveness across all device types.

### User Experience Design
- Ensure consistent visibility and functionality of the menu across all pages.
- Utilize descriptive and clear naming for pages.
- Implement intuitive visual cues for site navigation.
- Align website design with standard e-commerce practices.

### Content Strategy
- Clearly state the purpose and title of the website.
- Provide detailed information about Sanda Bazaar, including its background, location, and contact details.
- Organize and present bazaar information attractively.

### Feature Enhancement
- Establish a product list, categorized for easy navigation.
- Develop a functional shopping bag for product selection and modification.
- Offer a wishlist feature for personalized customer experiences.
- Enable product review functionality, allowing feedback and ratings.
- Introduce a streamlined checkout process.
- Create user profiles for managing delivery details and viewing past orders.
- Implement a newsletter subscription for promotional updates.
- Build a comprehensive admin dashboard for effective order and product management.

### Account Differentiation
- Give customers exclusive rights to add and edit product reviews, with view-only access for staff.
- Allow only customers to manage their wishlists.
- Restrict shopping bag functionalities to registered users and guests.
- Enable order placement solely for customers and guests.
- Limit product catalog management to staff.
- Make user profiles accessible to customers for personal details management.
- Offer wishlist functionality only to registered customers.
- Grant order overview and management capabilities exclusively to staff.

[Back to top ⇧](#overview)

## Structure

The structure of Sanda Bazaar's website is designed to cater to different user types, with content varying based on authentication and whether the user is a client or an admin.

### Register/Login
- Users can create an account and authenticate to access various features.

### Logout
- A modal feature that allows users to securely exit their account.

### Home
- Accessible to all users, it includes information about Sanda Bazaar, its open times, and products from the shop.

### All Products
- Displays a comprehensive list of all products available for sale.

### Product Categories
- Users can access products grouped by categories, such as Candles, Soaps, Instruments, etc.

### Product Details
- Shows full specifications for each product, including a review feature. Non-admin users can add products to their shopping bag, while staff members can edit or remove products.

### Profile 
- Available only to authenticated users, providing access to personal delivery details and order history.

### Profile Order Details
- Allows users to view full details of their own orders.

### Wishlist 
- Contains a list of products added by the user, inaccessible to guests or admin use

### Bag 
- Shows all items in the shopping bag, along with associated feature
- Includes an order summary and a form for personal, delivery, and payment details.

### Checkout Success
- Displays details of successfully completed orders.

### Orders Admin
- Accessible only to staff members, showing all orders placed, grouped and filtered by day.

### Admin Order Details
- Allows staff members to view full specifications of any order.

This structure ensures that Sanda Bazaar's website is user-friendly and efficiently meets the needs of different user types, from casual browsers to administrative staff.

[Back to top ⇧](#overview)

## Surface

### Sanda Bazaar Color Scheme and Typography

### Color Palette
![Color Palette Image](readme/colors.png)

Sanda Bazaar utilizes a warm and inviting color scheme that reflects its culturally rich atmosphere. The primary colors include:

- **Light Sand (#fff3e0)**: A soft and creamy shade, creating a light, airy feel.
- **Dark Sand (#a8742f)**: A deep, earthy tone that adds warmth and depth.
- **Sand Light (#f3c893)**: A muted, sandy hue for balance and versatility.
- **Black (#000000)**: Bold and classic, providing strong contrast.

### Typography
For its typography, Sanda Bazaar employs the Google font 'Eczar', a serif font. This choice enhances readability and adds an elegant touch to the overall design. The font's distinctive style contributes to the bazaar's unique and culturally enriched online presence.

```css
body {
  font-family: 'Eczar', serif;
}
```
[Back to top ⇧](#overview)

## Business Model

### Value Proposition
- **Passion-Driven Products**: Offering a curated selection of items that reflect the passions and interests of the Sanda Bazaar team.
- **Summer Shop Experience**: A serene spot for customers to enjoy coffee and a biscuit, emphasizing relaxation and enjoyment.
- **Exclusive Pre-Loved Market**: A specially selected range of valuable pre-loved items, available online at the end of each summer season.

### Customer Segments
- **Lifestyle Enthusiasts**: Individuals seeking unique, passion-driven products that reflect a love for life and culture.
- **Relaxation Seekers**: Visitors to the summer shop looking for a peaceful and enjoyable experience.
- **Collectors and Treasure Hunters**: Customers interested in exclusive, valuable pre-loved items.

### Channels
- **E-commerce Platform and Physical Store**: Both online and physical presence for a comprehensive shopping experience.
- **Social Media and Digital Marketing**: Utilizing digital platforms to connect with customers and promote products and experiences.
- **Email Newsletters**: Regular updates on new collections, summer shop highlights, and pre-loved market deals.

### Customer Relationships
- **Personalized Engagement**: Creating a welcoming atmosphere both online and at the summer shop, with a focus on customer enjoyment and satisfaction.
- **Exclusive Offers**: Providing access to special items and experiences for loyal customers.

### Revenue Streams
- **Diverse Product Sales**: Income from the sale of a wide range of products that the team loves.
- **Summer Shop Sales**: Revenue generated from the sale of refreshments and snacks at the summer shop.
- **Pre-Loved Market**: Earnings from the sale of exclusive pre-loved items at the end-of-season online market.

### Key Activities
- **Product and Experience Curation**: Handpicking products and creating enjoyable experiences that align with the team's passions.
- **Customer Experience Management**: Ensuring a high-quality, enjoyable experience both online and at the summer shop.
- **Pre-Loved Market Management**: Selecting and preparing valuable items for the end-of-season online sale.

### Key Resources
- **Unique Product Inventory**: A selection of products that reflects the team's interests and passions.
- **Summer Shop Setup**: A well-maintained and inviting space for the summer shop.
- **E-commerce Platform**: A robust online platform to facilitate e-commerce and pre-loved end-of-summer sales.

### Key Partnerships
- **Product Suppliers**: Partnerships with suppliers who provide unique and interesting products.
- **Local Artisans and Vendors**: Collaborations with local artisans for exclusive items.

### Cost Structure
- **Inventory and Purchasing**: Costs related to acquiring and maintaining a diverse product range.
- **Shop Operation**: Expenses for running the summer shop, including supplies and staffing.
- **Marketing and Promotion**: Investment in marketing activities to attract and retain customers.

This business model encapsulates Sanda Bazaar's dedication to selling products we love, offering a peaceful summer shop experience, and providing an exclusive online pre-loved end-of-summer market.

[Back to top ⇧](#overview)

## Marketing

### Overview
Our marketing strategy is designed to leverage both digital and local platforms, focusing on building a strong social media presence and engaging with the community, while planning for future expansion in advertising.

### Social Media Presence
- **Facebook and Instagram**: These platforms will be the primary focus for our digital marketing efforts. We'll use them to showcase our products, share stories about our summer shop, and engage with our community.
  - Regular posts featuring new products, behind-the-scenes content, and summer shop highlights.
  - Interactive campaigns to encourage user engagement and sharing.
  - Utilizing Instagram stories and reels to create dynamic and engaging content.

### Email Newsletters
- A regular newsletter to keep subscribers informed about new products, special events at the summer shop, and exclusive offers.
- Encouraging website visitors and summer shop customers to subscribe for the latest updates and deals.

### Local Community Engagement
- Participating in local Facebook groups to connect with the community and promote our products and summer shop.
- Engaging with local customers and visitors through community events and collaborations.

### Future Advertising Plans
- **DestinationGotland Ferry TV Screens**: Once the summer shop is operating successfully, we plan to run ads on the TV screens aboard the DestinationGotland ferry.
  - These ads will target tourists and locals traveling to and from Gotland, introducing them to Sanda Bazaar and inviting them to visit our summer shop.

### Measurable Goals
- Track engagement and conversion rates from social media campaigns.
- Monitor growth in newsletter subscriptions and engagement levels.
- Assess the impact of local community engagement on summer shop foot traffic and sales.
- Evaluate the effectiveness of TV screen advertising once implemented.

This marketing strategy is designed to build Sanda Bazaar's brand awareness and customer base, leveraging the power of social media, community engagement, and targeted advertising to attract and retain customers.

[Back to top ⇧](#overview)

## SEO Strategy for Sanda Bazaar
Given the relatively low competition in SEO for Gotland-related content, Sanda Bazaar has a unique opportunity to establish a strong online presence. The following meta tags are optimized to leverage this advantage:

### Keywords Integration

#### Local and Cultural Focus
- `Gotland products`
- `Gotland bazaar`
- `cultural items Gotland`
- `Gotland artisan market`
- `Gotland handmade goods`

#### Summer Shop and Cafe
- `summer shop Gotland`
- `cafe in Gotland`
- `best coffee Gotland`
- `relaxing cafe Gotland`
- `peaceful coffee spot Gotland`

#### Second-Hand Market
- `second-hand market Gotland`
- `unique finds Gotland`
- `exclusive second-hand Gotland`

#### Tourist Attraction
- `Gotland tourist shop`
- `must-visit in Gotland`
- `destination Gotland shopping`

#### Online Presence
- `online shopping Gotland`
- `Gotland e-commerce`
- `Gotland gifts online`
- `buy Gotland products online`

#### Local Engagement
- `Gotland community market`
- `local bazaar Gotland`
- `Gotland local artisans`
- `support local Gotland`

### SEO and Content Strategy

- **Social Media**: Use keywords in posts for product promotion and event marketing.
- **Google My Business**: List physical location with relevant keywords.
- **Website Optimization**: Include keywords in meta tags, product descriptions, and content.

### Blog Content Strategy for Sanda Bazaar

Sanda Bazaar's blog will play a crucial role in boosting SEO and engaging visitors with valuable content. The focus will be on creating content that not only resonates with our audience but also leverages high-ranking topics related to Gotland.

### Key Focus Areas

#### 1. Linking to High-Ranking Gotland Sites
- **Strategic Partnerships**: Collaborate with or reference popular local sites like Destination Gotland.
- **Backlinking**: Include backlinks to high-ranking websites related to Gotland to enhance SEO and provide readers with valuable resources.

#### 2. Topics Related to Gotland
- **Local Insights**: Share unique insights, stories, and experiences about Gotland to attract readers interested in the region.
- **Travel and Tourism**: Post articles about traveling to and within Gotland, including tips, guides, and highlights of local attractions.

#### 3. Incorporating High-Ranking Keywords
- **Keyword Research**: Regularly research and integrate high-ranking keywords related to Gotland into our blog posts.
- **SEO Optimization**: Optimize each blog post with relevant keywords, meta descriptions, and tags to improve search engine rankings.

#### 4. Engaging and Informative Content
- **Quality Content**: Ensure each blog post is informative, engaging, and aligns with our audience's interests.
- **Regular Updates**: Maintain a consistent blogging schedule to keep our content fresh and encourage repeat visits.

### Measuring Success
- **Analytics**: Use tools like Google Analytics to track the performance of our blog posts, including visitor numbers, engagement rates, and referral sources.
- **Feedback**: Encourage and monitor reader comments and feedback to gauge the effectiveness of our content and adapt our strategy accordingly.

This content strategy aims to strengthen Sanda Bazaar's online presence, with a particular emphasis on showcasing and connecting with the Gotland community.

[Back to top ⇧](#overview)

## Agile Methodology

As a solo student embarking on this project, I've embraced a practical Agile approach to reach a Minimum Viable Product (MVP). This journey involved seven sprints, with the final, 7th sprint dedicated primarily to testing and bug fixing. This strategic focus ensures ample time to refine the project and guarantee its functionality.

While I recognize that my real-world project demands extensive work, I've deliberately kept this endeavor project-focused. This allows for a structured development process that can evolve as the project progresses.

I have established a Kanban board, organizing user stories and tasks in a sequential order of completion. This structure not only helps me track my progress but also ensures that I adhere to my original vision. Each task and EPIC added to the board reflects my commitment to fulfilling the foundational user stories and the overarching EPICs outlined in this README.

The goal has always been to achieve an MVP for this project. However, I'm aware that transitioning to an actual store launch entails much more development. This project will continue to evolve in a separate fork, highlighting the journey from MVP to a fully-fledged product launch.

Working in an Agile manner has taught me the importance of foresight and planning. Historically, planning wasn't my forte, but through development, I've learned its value. The Agile framework has been instrumental in preventing last-minute rushes and overwhelming workloads. I'm continuously exploring new Agile tools to enhance my planning process, making it more fluid and effective.

This learning journey in Agile methodology underscores the power of structured planning in software development. It's a journey of continuous improvement, learning, and adaptation.


[My Kanban Board](https://github.com/users/birgerosterberg/projects/4/)


[Back to top ⇧](#overview)

## Features
<details>
<summary style="font-size: larger;">Navbar Desktop and Mobile</summary>

- **Large & XL Screens:**
  - Always-visible search box for product searches by name and description.
  - Account Menu with links varying by login status and admin rights, including sign-in, profile, and site management.
  - Shopping bag icon displaying current bag contents and total value, with dynamic styling based on contents.
  - Home page and products dropdown links, including category-specific views.

- **Medium & Smaller Screens:**
  - Dropdown burger icon for compact navigation.
  - Links to home, products, and more, similar to larger screens.
  - Search icon triggering a dropdown search bar.
  - Account and shopping bag features similar to larger screens.

- **My Account Link Variations:**
  - Different types of links are available depending on the user's status:
    - Admin users get access to advanced site management options.
    - Logged-in users see personalized account options.
    - Not logged-in users are presented with options to sign-in or register.

  <details>
  <summary>Images Desktop Navbar</summary>

  ![Navbar Account Bag Desktop](readme/navbar-feat/navbar-acc-bag-d.png)
  ![Navbar Account Dropdown Desktop](readme/navbar-feat/navbar-acc-dropdown-d.png)
  ![Navbar Dropdown Desktop](readme/navbar-feat/navbar-dropdown-d.png)
  ![Navbar Links Desktop](readme/navbar-feat/navbar-links-d.png)
  ![Navbar Logo Desktop](readme/navbar-feat/navbar-logo-d.png)
  ![Navbar Search Desktop](readme/navbar-feat/navbar-search-d.png)
  ![Navbar Logged in User](readme/navbar-feat/logged-in-user.png)
  ![Navbar Not Logged in](readme/navbar-feat/not-loggedin.png)
  </details>

  <details>
  <summary>Images Mobile Navbar</summary>

  ![Navbar Account Bag Mobile](readme/navbar-feat/navbar-acc-drop-m.png)
  ![Navbar Hamburger Links Mobile](readme/navbar-feat/navbar-ham-links-m.png)
  ![Navbar Hamburger Links Search Mobile](readme/navbar-feat/navbar-ham-links-search-m.png)

  </details>
</details>

<details>
<summary style="font-size: larger;">Open Times</summary>

- **Dynamic Display:**
  - Automatically checks the current day and displays corresponding open times.
  - If the shop is closed on a particular day, it shows "We're closed today."
  - Used for displaying weekly open times on both the Home and Contact pages.

- **Admin Panel Management:**
  - Open times for each day can be easily set and updated from the admin panel.
  - Eliminates the need for manual HTML changes, ensuring ease of management.

- **Customer Convenience:**
  - Provides visitors with accurate and up-to-date opening hours.
  - Particularly useful for local and visiting customers in Gotland, addressing common issues with changing open times.
  - Enhances the user experience on the Home and Contact pages by providing clear open time information.

- **Responsive Design:**
  - Seamlessly adapts to different devices, ensuring accessibility for all users.

- **Value to Customers:**
  - Ensures customers always have the most current information on shop availability.
  - Enhances user experience by offering clear, instant insights into shop open times.

  <details>
  <summary>Images Open Times</summary>

  ![Daily Open Time](readme/open/opentime.png)
  ![Weekly Open Time](readme/open/weekopen.png)
  ![Open time Admin](readme/open/openadmin.png)

  </details>
</details>

<details>
<summary style="font-size: larger;">Blog Functionality</summary>

- **Homepage Sneak Peek:**
  - Features a snippet and link to the latest blog post, designed to pique visitor interest.

- **Blog Page:**
  - Displays an image along with the full text of each blog post.

- **Admin Management with Summernote for Django:**
  - The blog post editor uses Summernote, a rich text editor for Django, enhancing the content creation experience.
  - Provides an easy-to-use interface for creating and editing blog posts.
  - Offers an overview of all blog posts and simplifies the process of adding new blog posts.
  <details>
  <summary>Blog images</summary>
  
  ![Blog snippet homepage](<readme/blog/home blogpost.png>)
  ![Blog page view](readme/blog/blog-page.png)
  ![Blog admin overview](readme/blog/overview-blog-a.png)
  ![Blog post view](readme/blog/admin-blogpost.png)
 
  </details>
</details>


[Back to top ⇧](#overview)

---

## Database

<details>
<summary>Category Model</summary>

- name: `CharField` (max_length=254)
- friendly_name: `CharField` (max_length=254, null=True, blank=True)
</details>

<details>
<summary>Product Model</summary>

- category: `ForeignKey` to 'Category' (null=True, blank=True)
- sku: `CharField` (max_length=254, null=True, blank=True)
- name: `CharField` (max_length=254)
- description: `TextField`
- price: `DecimalField` (max_digits=6, decimal_places=2)
- rating: `DecimalField` (max_digits=6, decimal_places=2, null=True, blank=True)
- image_url: `URLField` (max_length=1024, null=True, blank=True)
- image: `ImageField` (null=True, blank=True)
</details>

<details>
<summary>BlogPost Model</summary>

- title: `CharField` (max_length=200)
- content: `TextField`
- published_date: `DateTimeField` (auto_now_add=True)
- image: `ImageField` (upload_to='blog_images/', blank=True, null=True)
</details>

<details>
<summary>OpeningHours Model</summary>

- monday: `CharField` (max_length=50, blank=True)
- tuesday: `CharField` (max_length=50, blank=True)
- wednesday: `CharField` (max_length=50, blank=True)
- thursday: `CharField` (max_length=50, blank=True)
- friday: `CharField` (max_length=50, blank=True)
- saturday: `CharField` (max_length=50, blank=True)
- sunday: `CharField` (max_length=50, blank=True)
</details>

<details>
<summary>UserProfile Model</summary>

- user: `OneToOneField` to 'User' (on_delete=models.CASCADE)
- default_phone_number: `CharField` (max_length=20, null=True, blank=True)
- default_street_address1: `CharField` (max_length=80, null=True, blank=True)
- default_street_address2: `CharField` (max_length=80, null=True, blank=True)
- default_town_or_city: `CharField` (max_length=40, null=True, blank=True)
- default_county: `CharField` (max_length=80, null=True, blank=True)
- default_postcode: `CharField` (max_length=20, null=True, blank=True)
- default_country: `CountryField` (blank_label='Country', null=True, blank=True)
</details>

<details>
<summary>Review Model</summary>

- product: `ForeignKey` to 'Product' (on_delete=models.CASCADE)
- user: `ForeignKey` to 'User' (on_delete=models.CASCADE)
- review_text: `TextField`
- rating: `IntegerField`
- created_at: `DateTimeField` (auto_now_add=True)
</details>

<details>
<summary>Wishlist Model</summary>

- user: `OneToOneField` to 'User' (on_delete=models.CASCADE)
- products: `ManyToManyField` to 'Product'
</details>

<details>
<summary>Checkout Model</summary>

- Order:
  - order_number: `CharField` (max_length=32, null=False, editable=False)
  - user_profile: `ForeignKey` to 'UserProfile' (on_delete=models.SET_NULL, null=True, blank=True)
  - full_name: `CharField` (max_length=50, null=False, blank=False)
  - email: `EmailField` (max_length=254, null=False, blank=False)
  - phone_number: `CharField` (max_length=20, null=False, blank=False)
  - country: `CountryField` (blank_label='Country *', null=False, blank=False)
  - postcode: `CharField` (max_length=20, null=True, blank=True)
  - town_or_city: `CharField` (max_length=40, null=False, blank=False)
  - street_address1: `CharField` (max_length=80, null=False, blank=False)
  - street_address2: `CharField` (max_length=80, null=True, blank=True)
  - county: `CharField` (max_length=80, null=True, blank=True)
  - date: `DateTimeField` (auto_now_add=True)
  - delivery_cost: `DecimalField` (max_digits=6, decimal_places=2, null=False, default=0)
  - order_total: `DecimalField` (max_digits=10, decimal_places=2, null=False, default=0)
  - grand_total: `DecimalField` (max_digits=10, decimal_places=2, null=False, default=0)
  - original_bag: `TextField` (null=False, blank=False, default='')
  - stripe_pid: `CharField` (max_length=254, null=False, blank=False, default='')

- OrderLineItem:
  - order: `ForeignKey` to 'Order' (null=False, blank=False, on_delete=models.CASCADE)
  - product: `ForeignKey` to 'Product' (null=False, blank=False, on_delete=models.CASCADE)
  - quantity: `IntegerField` (null=False, blank=False, default=0)
  - lineitem_total: `DecimalField` (max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
</details>

![Database Model DrawSQL](readme/drawSQL-sanda-bazaar.png)

## Responsive Layout and Design
[Link to separate testing readme](/TESTING.md)

[Back to top ⇧](#overview)


## Technologies Used
*List all the technologies, languages, frameworks, and tools used.*
[Back to top ⇧](#overview)


## Testing
[Link to separate testing readme](/TESTING.md)

[Back to top ⇧](#overview)


## Deployment

### Database (ElephantSQL)
1. Navigate to the [ElephantSQL website](https://www.elephantsql.com/) and log in.
2. Click on "Create New Instance" in the top-right corner.
3. Enter a database name, leave the plan field as is, optionally enter tags.
4. Select your region, click "Review", and then "Create instance".
5. In your dashboard, find the newly created database instance and click on it.
6. Copy the URL starting with `postgres://`.
7. Paste this URL into `env.py` file as `DATABASE_URL` value:

   ```python
   os.environ["DATABASE_URL"] = "postgres://yourLinkFromDatabaseDashboard"

### Django Secret Key
- To secure the Django app, set the secret key as an environment variable:

  ```python
  os.environ["SECRET_KEY"] = "yourSecretKey"

### Deploying on Heroku
1. **Create a New App on Heroku**:
   - Navigate to [Heroku](https://heroku.com/), log in and open the dashboard.
   - Click "New" > "Create new app".
   - Enter your app name, choose a region, and click "Create app".

2. **Connect to GitHub**:
   - In the "Deploy" tab, go to "Deployment method" section.
   - Authorize and connect your GitHub account, then select your repository.

3. **Set Configuration Variables**:
   - Go to the "Settings" tab and click "Reveal Config Vars".
   - Add the following keys and values:
     | Key                    | Value                                 |
     |------------------------|---------------------------------------|
     | AWS_ACCESS_KEY_ID      | `aws url beginning with aws://`       |
     | DATABASE_URL           | `postgress url beginning with postgress://` |
     | DISABLE_COLLECTSTATIC  | `1`                                   |
     | SECRET_KEY             | `YourSecretKey`                       |

   - Note: `DISABLE_COLLECTSTATIC` should be `1` for initial deployment and removed before final deployment.

4. **Update Django Settings**:
   - In `settings.py`, update `ALLOWED_HOSTS` with your Heroku app's URL.

5. **Prepare for Deployment**:
   - Ensure `Procfile` is correct, e.g., `web: gunicorn sanda_bazaar.wsgi:application`.
   - Create a `runtime.txt` file in your project root.
   - Push changes to GitHub.
   - Specify the Python version, `python-3.11.4`.

6. **Manual Deploy**:
   - In Heroku's "Deploy" tab, under "Manual deploy", select the main branch and click "Deploy Branch".

7. **Final Deployment Steps**:
   - Remove `DISABLE_COLLECTSTATIC` variable in Heroku's settings.

8. **Access Deployed App**:
   - After build completion, access your app via the provided link.

[Back to top ⇧](#overview)

## AWS (Amazon Web Services) Setup for Sanda Bazaar

AWS is utilized for storing all static and media files of Sanda Bazaar.

### S3 Bucket Setup
1. **Create an AWS Account**: 
   - Sign up or log in at [AWS](https://aws.amazon.com/).

2. **Create and Configure an S3 Bucket**: 
   - In AWS, navigate to S3 (All Services > Storage > S3).
   - Click 'Create Bucket'.
   - Name the bucket (using the project's name is recommended), select your region.
   - In 'Object Ownership', select 'ACLs enabled'.
   - Uncheck 'Block all public access'.
   - Enable 'Static website hosting' in the bucket properties.
   - Set CORS Configuration:
     ```json
     [
         {
             "AllowedHeaders": ["Authorization"],
             "AllowedMethods": ["GET"],
             "AllowedOrigins": ["*"],
             "ExposeHeaders": []
         }
     ]
     ```

3. **Set Bucket Policy and Permissions**:
   - Use the AWS Policy Generator to create an S3 Bucket Policy (select 'S3 Bucket Policy').
   - Allow all principals (`*`) and select 'Get object'.
   - Paste your Bucket ARN into the policy generator and append `/*` to the resource key.
   - In the ACL section, grant 'list' access to 'Everyone (public access)'.

### IAM (Identity and Access Management) Configuration
1. **Create a User Group and Policy**:
   - In IAM, create a user group (e.g., 'manage-your-project-name').
   - Create a policy with S3 full access, customized with your bucket's ARN.

2. **Create an IAM User**:
   - Add a new user with programmatic access to your group.
   - Download the CSV file containing access keys.

#### Connecting AWS to django

Now that you have created a S3 bucket with its user group attached, we need to connect it to django.

1. First you will need to install two packages. Boto3 and Django storages. Do this by running these commands:  
    ```
    pip3 install boto3
    pip3 install django-storages
    ```
    And remember to freeze the requirements with:  
    ```
    pip3 freeze > requirements.txt
    ```
2. You will then need to add 'storages' to your installed apps section inside your settings.py file. Do that now. 
3. Next, we will need to add some additional settings to the same file to let django know what bucket it's communicating with. 
4. Somewhere near the bottom of the file you should write an if statement to check if there is an environment variable called USE_AWS. This variable does not exist yet but we will add it later. Inside the if statement, write the following settings so it looks like this:  
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
        AWS_S3_REGION_NAME = 'insert-your-region-here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
5. Next, hop back to heroku and in the settings tab, under config vars, you will need to add some keys with values that were downloaded earlier in the CSV file.
6. Add the key, AWS_ACCESS_KEY_ID with the value that was generated in the CSV file earlier. Then add the key AWS_SECRET_ACCESS_KEY, and again add the value that was generated in the CSV file. Once they have both been added, add the key USE_AWS, and set the value to True.
7. You can now also remove the DISABLE_COLLECTSTAIC variable, since django should now collect static files automatically and upload them to S3.
8. Now head back to the settings.py file in your django project and head back to the if statement we wrote earlier and inside the statement add this line setting:  
    ```
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
    This is to tell django where our static files will be coming from in production.
9. Next we need to create a file to tell django that we want to use S3 to store our static files whenever someone runs collectstatic and also that we want any uploaded product images to go there also.
10. In the root directory of your project create a file called 'custom_storages.py'. Inside this file you will need to import your settings as well as the s3boto3 storage class. So at the top of the file insert the code:  
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    ```
11. Then underneath the imports insert these two classes:  
    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
    The STATICFILES_LOCATION and MEDIAFILES_LOCATION have yet to be defined, so lets do that now.
12. Back in the settings.py file, underneath the bucket config settings but still inside the if statement, add these lines:  
    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
13. Next, you will also need to override and explicitly set the URLs for static and media files using your custom domain and new locations. To do this add these two lines inside the same if statement:  
    ```
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
14. If you now save, add, commit and push your changes, you should see that your S3 bucket now has a static folder with all your static files inside. Next, we need to handle the Media files but first, inside the if statement add the following code. This helps to speed things up by letting the browser know that its ok to cache static files for a long time:    
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    ```
15. Back in S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
16. Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
17. Then under 'Permissions' select the option 'Grant public-read access' and click upload. You may need to also check an acknowledgment warning checkbox too. 
18. Once that is finished you're all set. All your static files and media files should be automatically linked from django to your S3 bucket.missions to 'public-read' during upload.

[Back to top ⇧](#overview)


### Stripe

Stripe is needed to handle the checkout process when a payment is made. You will need a stripe account which you can sign up for [here](https://stripe.com/en-gb).

#### Payments

1. To set up stripe payments you can follow their guide [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

#### Webhooks

1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
2. Then in the side-nav under the Developers title, click on 'Webhooks', then 'Add endpoint'.
3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:  
    ```
    https://your-app-name.herokuapp.com/checkout/wh/
    ```
4. Then click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
6. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
7. Add these values under these keys:  
    ```
    STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
    STRIPE_SECRET_KEY = 'insert your secret key'
    STRIPE_WH_SECRET = 'insert your webhooks secret key'
    ```
8. Finally, back in your setting.py file in django, insert the following near the bottom of the file:  
    ```
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```
[Back to top ⇧](#overview)

## Credits
*Acknowledge anyone or any resources that helped in my project.*