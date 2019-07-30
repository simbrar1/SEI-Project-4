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
    // const error = { ...this.state.error, [name]: '' }
    this.setState({ data, error: '' })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        console.log(res.data)
        this.props.history.push('/')
      })
      .catch(() => this.setState({ error: 'Invalid Credentials' }))
  }


  render() {
    console.log(this.state.error)
    return (
      <main className="section">
        <div className="card auth">
          <form className="form-horizontal" onSubmit={this.handleSubmit}>
            <div className="form-group">
              <div className="col-2 col-sm-12">
                <label className="form-label" htmlFor="email">Email</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.error ? 'text-red border-red' : ''} `}
                  name="email"
                  type="text"
                  placeholder="Email"
                  onChange={this.handleChange}/>
              </div>

            </div>
            <div className="form-group">
              <div className="col-2 col-sm-12">
                <label className="form-label" htmlFor="password">Password</label>
              </div>
              <div className="col-4 col-sm-12">
                <input
                  className={`form-input ${this.state.error ? 'text-red border-red' : ''} `}
                  name="password"
                  type="password"
                  placeholder="Password"
                  onChange={this.handleChange}/>
              </div>
            </div>
            {this.state.error && <small className="text-red">{this.state.error}</small>}
            <div className="auth-btn">
              <button className="btn btn-sm">Login</button>
            </div>
          </form>
        </div>
      </main>

    )
  }

}

export default Login
