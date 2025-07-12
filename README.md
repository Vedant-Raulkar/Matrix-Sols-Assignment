# Collage Editor Platform

A web-based application where users can upload multiple images and generate visually aligned collage layouts. The platform allows users to preview and save their image sets in an organized manner with complete user authentication.

## Features

### Backend Features (Django)
- **User Authentication**: Complete registration, login, logout system
- **Models**: 
  - `Collage`: Stores collage information with title, creation date, template ID, and frame style
  - `ImageItem`: Stores individual images linked to collages with positioning data and order
- **Views**: Full CRUD operations for collages with user-specific access
- **Forms**: Multi-image upload with validation (max 10 images per collage)
- **Media Handling**: Proper image storage and serving

### Frontend Features (HTML, CSS, JavaScript)
- **Aesthetic UI**: Modern Bootstrap-based design with custom styling
- **Upload Interface**: Clean form with drag-and-drop image preview
- **Multiple Template Types**: Various collage templates (template_2_1, etc.)
- **Frame Styles**: Modern, Classic, Minimal, and Vintage frame options
- **Image Positioning**: Flexible positioning with coordinates and dimensions
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Export Functionality**: Download collages as PNG images using HTML2Canvas

### Advanced Features
- **User-specific Access**: Users can only see and edit their own collages
- **Flexible Positioning**: Images can be arranged in any direction/orientation
- **Drag & Drop**: Real-time image repositioning in freeform mode
- **Search & Pagination**: Find collages easily with search and pagination
- **AJAX Updates**: Seamless position updates without page refresh

## Setup Instructions

### Prerequisites
- Python 3.8+ installed
- pip package manager
- Git (optional, for cloning)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd collage_editor_platform
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Getting Started
1. **Register**: Create a new account or log in with existing credentials
2. **Create Collage**: Click "Create New" to start a new collage
3. **Upload Images**: Select multiple images from your device
4. **Choose Template**: Select from available collage templates
5. **Choose Frame Style**: Pick from Modern, Classic, Minimal, or Vintage styles
6. **Save & View**: Save your collage and view the details

### Template and Frame Options

#### Templates
- Various pre-designed collage templates
- Customizable layout arrangements
- Template-based positioning system

#### Frame Styles
- **Modern**: Clean, contemporary styling
- **Classic**: Traditional, elegant borders
- **Minimal**: Simple, understated design
- **Vintage**: Retro, nostalgic appearance


### Key Features

#### User Authentication
- Secure registration and login
- Password management
- User profile with statistics
- Session management

#### Collage Management
- Create, read, and delete collages
- Search functionality for finding collages
- Pagination for large collections
- User-specific access control

#### Image Handling
- Support for JPEG, PNG, GIF, WebP formats
- Automatic image optimization
- Responsive image display
- Secure file upload validation

#### Viewing Options
- Detailed collage view with all images
- Responsive image display
- Clean, organized layout

## Project Structure

```
collage_editor_platform/
├── collage_platform/          # Main Django project
│   ├── settings.py           # Django settings
│   ├── urls.py              # URL configuration
│   └── wsgi.py              # WSGI configuration
├── collages/                 # Collages app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin interface
├── accounts/                 # User authentication app
│   ├── views.py             # Authentication views
│   └── urls.py              # Authentication URLs
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── collages/            # Collage templates
│   ├── accounts/            # Account templates
│   └── registration/        # Auth templates
├── static/                  # Static files
│   ├── css/                 # Stylesheets
│   └── js/                  # JavaScript files
├── media/                   # User uploads
│   └── collages/            # Uploaded images
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technical Details

### Backend Architecture
- **Framework**: Django 4.2.13
- **Database**: SQLite (development) - easily changeable for production
- **Image Processing**: Pillow for image handling
- **Authentication**: Django's built-in authentication system

### Frontend Technologies
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Bootstrap Icons
- **JavaScript**: Vanilla JS with jQuery
- **Image Export**: HTML2Canvas library
- **Responsive Design**: Mobile-first approach

### Security Features
- CSRF protection on all forms
- User-specific data access
- File upload validation
- Secure media file handling
- Session-based authentication

## Database Schema

### Collage Model
- `id`: Primary key
- `title`: Collage title (max 255 chars)
- `user`: Foreign key to User model
- `created_at`: Auto-generated timestamp
- `template_id`: Template identifier (default: 'template_2_1')
- `frame_style`: Frame style choice (modern/classic/minimal/vintage)

### ImageItem Model
- `id`: Primary key
- `collage`: Foreign key to Collage
- `image`: Image file field
- `caption`: Optional image caption
- `order`: Display order
- `x_position`, `y_position`: Freeform positioning
- `width`, `height`: Custom dimensions

## API Endpoints

### Authentication
- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/accounts/profile/` - User profile

### Collages
- `/` - Home page
- `/collages/` - List all user collages
- `/collages/create/` - Create new collage
- `/collages/<id>/` - View collage detail
- `/collages/<id>/delete/` - Delete collage

## Customization

### Adding New Templates or Frame Styles
1. Update `template_id` options or `frame_style` choices in `models.py`
2. Add corresponding CSS in `static/css/style.css`
3. Update template logic in `detail.html`
4. Add form options in `forms.py`

### Styling Customization
- Modify `static/css/style.css` for visual changes
- Update Bootstrap variables for theme changes
- Add custom JavaScript in template blocks

### Feature Extensions
- Add image filters and effects
- Implement collaborative collages
- Add social sharing features
- Include image annotation tools

## Troubleshooting

### Common Issues

1. **Images not displaying:**
   - Check MEDIA_URL and MEDIA_ROOT settings
   - Ensure media files are served correctly
   - Verify file permissions

2. **Upload errors:**
   - Check file size limits
   - Verify supported file formats
   - Ensure proper form encoding

3. **Layout issues:**
   - Clear browser cache
   - Check CSS file loading
   - Verify responsive breakpoints

### Debug Mode
- Set `DEBUG = True` in settings.py for development
- Check Django debug toolbar for performance issues
- Use browser developer tools for frontend debugging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review Django documentation
3. Search existing issues
4. Create a new issue with detailed description

## Future Enhancements

- [ ] Add image filters and effects
- [ ] Implement real-time collaboration
- [ ] Add social sharing capabilities
- [ ] Include image annotation tools
- [ ] Add collage templates
- [ ] Implement image search and tagging
- [ ] Add export to different formats (PDF, SVG)
- [ ] Mobile app development
- [ ] Cloud storage integration
- [ ] Advanced layout algorithms
