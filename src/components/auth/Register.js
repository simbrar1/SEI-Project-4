import React from 'react'
import axios from 'axios'

class Register extends React.Component {
  constructor() {
    super()


    this.state = { data: {}, errors: {}  }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    const errors = { ...this.state.errors, [name]: '' }
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch(err => this.setState({ errors: err.response.data }))
  }

  render() {
    return (
      <main className="section">
        <div className="card auth">
          <form className="form-horizontal" onSubmit={this.handleSubmit}>
            <div className="form-group">
              <div className="col-3 col-sm-12">
                <label className="form-label" htmlFor="email">Username</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.errors.username ? 'text-red border-red' : ''} `}
                  name="username"
                  type="text"
                  placeholder="username"
                  onChange={this.handleChange}/>
              </div>
              {this.state.errors.username && <small className="text-red">{this.state.errors.username}</small>}
            </div>
            <div className="form-group">
              <div className="col-3 col-sm-12">
                <label className="form-label" htmlFor="email">Email</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.errors.email ? 'text-red border-red' : ''} `}
                  name="email"
                  type="text"
                  placeholder="Email"
                  onChange={this.handleChange}/>
              </div>
              {this.state.errors.email && <small className="text-red">{this.state.errors.email}</small>}
            </div>
            <div className="form-group">
              <div className="col-3 col-sm-12">
                <label className="form-label" htmlFor="email">Password</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.errors.password ? 'text-red border-red' : ''} `}
                  name="password"
                  type="password"
                  placeholder="Password"
                  onChange={this.handleChange}/>
              </div>
              {this.state.errors.password && <small className="text-red">{this.state.errors.password}</small>}
            </div>
            <div className="form-group">
              <div className="col-3 col-sm-12">
                <label className="form-label" htmlFor="email">Password Confirmation</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.errors.password_confirmation ? 'text-red border-red' : ''} `}
                  name="password_confirmation"
                  type="password"
                  placeholder="Password Confirmation"
                  onChange={this.handleChange}/>
              </div>
            </div>
            {this.state.errors.password_confirmation && <small className="text-red">{this.state.errors.password_confirmation}</small>}
            <div className="auth-btn">
              <button className="btn btn-sm">Register</button>
            </div>

          </form>
        </div>
      </main>
    )
  }
}

export default Register


// <main>
//   <section className="form-container">
//     <form onSubmit={this.handleSubmit}>
//       <h2 className="form-title">Register</h2>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.errors.username ? 'is-danger' : ''}`}
//             name="username"
//             placeholder="Username"
//             onChange={this.handleChange}
//           />
//         </div>
//         {this.state.errors.username && <small className="help is-danger">{this.state.errors.username}</small>}
//       </div>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.errors.username ? 'is-danger' : ''}`}
//             name="email"
//             placeholder="Email"
//             onChange={this.handleChange}
//           />
//         </div>
//         {this.state.errors.email && <small className="help is-danger">{this.state.errors.email}</small>}
//       </div>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.errors.password ? 'is-danger' : ''}`}
//             type="password"
//             name="password"
//             placeholder="Password"
//             onChange={this.handleChange}
//           />
//         </div>
//         {this.state.errors.password && <small className="help is-danger">{this.state.errors.password}</small>}
//       </div>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.errors.password_confirmation ? 'is-danger' : ''}`}
//             type="password"
//             name="password_confirmation"
//             placeholder="Password Confirmation"
//             onChange={this.handleChange}
//           />
//         </div>
//         {this.state.errors.password_confirmation && <small className="help is-danger">{this.state.errors.password_confirmation}</small>}
//       </div>
//       <button type="submit" className="button">Submit</button>
//     </form>
//   </section>
// </main>
