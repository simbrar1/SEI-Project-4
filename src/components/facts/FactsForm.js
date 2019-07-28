import React from 'react'

const FactsForm = ({ data, years, handleChange, handleSubmit}) => (
  <form onSubmit={handleSubmit}>
    <div className="form-group">
      <div className="col-7">
        <label className="form-label" htmlFor="input-example-">Name</label>
        <input className="form-input"
          name="name"
          type="text"
          placeholder="Name"
          onChange={handleChange}
          value={data.name || ''}
        />
      </div>
      <div className="col-7">
        <label className="form-label" htmlFor="input-example-">Location</label>
        <input className="form-input"
          name="location"
          type="text"
          placeholder="Location"
          onChange={handleChange}
          value={data.location || ''}
        />
      </div>
      <div className="col-7">
        <label className="form-label" htmlFor="input-example-">Date of Fact</label>
        <input className="form-input"
          name="date_of_fact"
          type="date"
          placeholder="Date"
          onChange={handleChange}
          value={data.date_of_fact || ''}
        />
      </div>
      <div className="col-7">
        <label className="form-label" htmlFor="input-example-">Fact Description</label>
        <textarea className="form-input"
          name="bio"
          rows="4"
          type="text"
          placeholder="Description"
          onChange={handleChange}
          value={data.bio || ''}
        />
      </div>
      <div className="col-7">
        <label className="form-label" htmlFor="input-example-">Image</label>
        <input className="form-input"
          name="image"
          type="text"
          placeholder="Image"
          onChange={handleChange}
          value={data.image || ''}
        />
      </div>
      <div className="col-7">
        <label
          className="form-label"
          htmlFor="input-example-"
        >
          Year
        </label>
        <select
          className="form-select"
          name="year_number"
          onChange={handleChange}
          defaultValue={data.year || ''}
        >
          <option disabled value="">Choose a Year</option>
          {years.map(year => (
            <option key={year} value={year}>{year}</option>
          ))
          }
        </select>

      </div>
    </div>
    <button className="btn btn-sm">Create</button>
  </form>
)

export default FactsForm
