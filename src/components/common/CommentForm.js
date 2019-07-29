import React from 'react'

const CommentForm = ({ text, handleCommentChange, handleCommentSubmit }) => (
  <form onSubmit={handleCommentSubmit}>
    <div className="field">
      <div className="control">
        <textarea
          className="textarea"
          placeholder="Comment......"
          onChange={handleCommentChange}
          name="text"
          value={text || ''}
        >
        </textarea>
      </div>
    </div>
    <button className="button" type="submit">Post Comment</button>
  </form>
)

export default CommentForm
