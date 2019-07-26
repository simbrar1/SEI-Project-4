import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'

class NavBar extends React.Component {
  constructor() {
    super()

    this.state = {}
    this.logout = this.logout.bind(this)
  }

  logout() {
    Auth.logout()
    this.props.history.push('/')
  }

  componentDidUpdate(prevProps) {
    if (this.props.location.pathname !== prevProps.location.pathname) {
      this.setState({ navbarOpen: false })
    }
  }

  render() {
    return (
      <div className="bg-dark">
        <ul className="tab tab-block">
          <li className="tab-item">
            <Link to="/" className="navbar-item">History Info</Link>
          </li>
          <li className="tab-item">
            {!Auth.isAuthenticated() && <Link to="/register" className="navbar-item">Register</Link>}
            {Auth.isAuthenticated() && <Link to="/new/facts" className="navbar-item">Create New Fact</Link>}
          </li>
          <li className="tab-item">
            {!Auth.isAuthenticated() && <Link to="/login" className="navbar-item">Login</Link>}
            {Auth.isAuthenticated() && <a className="navbar-item" onClick={this.logout}>Logout</a>}
          </li>



        </ul>
      </div>
    )
  }
}

export default withRouter(NavBar)


// render() {
//   return (
//     <nav className="navbar is-primary">
//       <div className="container">
//         <div className="navbar-brand">
//           <Link to="/" className="navbar-item">History Info</Link>
//           <a role="button" className={`navbar-burger ${this.state.navbarOpen ? 'is-active' : ''}`} aria-label="menu" aria-expanded="false" onClick={this.toggleNavbar}>
//             <span aria-hidden="true"></span>
//             <span aria-hidden="true"></span>
//             <span aria-hidden="true"></span>
//           </a>
//         </div>
//         <div className={`navbar-menu ${this.state.navbarOpen ? 'is-active' : ''}`}>
//           <div className="navbar-end">
//             <Link to="/register" className="navbar-item">Register</Link>
//             <Link to="/login" className="navbar-item">Login</Link>
//           </div>
//         </div>
//       </div>
//     </nav>
//   )
// }
// }
