import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: ''  }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: { name, value } }) {
    const data = { ...this.state.data, [name]: value }
    const errors = { ...this.state.errors, [name]: '' }
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        console.log(res.data)
        this.props.history.push('/')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }


  render() {
    return (
      <main className="section">
        <form className="form-horizontal" onSubmit={this.handleSubmit}>
          <div className="form-group">
            <div className="col-1 col-sm-12">
              <label className="form-label" htmlFor="email">Email</label>
            </div>
            <div className="col-4 col-sm-12">
              <input
                className="form-input"
                name="email"
                type="text"
                placeholder="Email"
                onChange={this.handleChange}/>
            </div>
          </div>
          <div className="form-group">
            <div className="col-1 col-sm-12">
              <label className="form-label" htmlFor="password">Password</label>
            </div>
            <div className="col-4 col-sm-12">
              <input
                className="form-input"
                name="password"
                type="password"
                placeholder="Password"
                onChange={this.handleChange}/>
            </div>
          </div>
          <button className="btn btn-sm">Login</button>
        </form>
      </main>

    )
  }

}

export default Login

// <main className="section">
//   <div className="form-container">
//     <form onSubmit={this.handleSubmit}>
//       <h2 className="form-title">Login</h2>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.error ? 'is-danger' : ''}`}
//             name="email"
//             placeholder="Email"
//             onChange={this.handleChange}
//           />
//         </div>
//       </div>
//       <div className="field">
//         <div className="control">
//           <input
//             className={`input ${this.state.error ? 'is-danger' : ''}`}
//             type="password"
//             name="password"
//             placeholder="Password"
//             onChange={this.handleChange}
//           />
//         </div>
//         {this.state.error && <small className="help is-danger">{this.state.error}</small>}
//       </div>
//       <button type="submit" className="button is-danger">Login</button>
//     </form>
//   </div>
// </main>
